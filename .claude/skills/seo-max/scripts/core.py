#!/usr/bin/env python3
"""
BM25 Search Engine for SEO Max

Implements BM25 ranking algorithm for searching across SEO knowledge base.
Based on UI/UX Pro Max architecture pattern.

Author: Abhinav Dobhal
License: MIT
"""

import csv
import math
import os
import re
from collections import Counter, defaultdict
from typing import List, Dict, Tuple, Optional


class BM25:
    """
    BM25 (Best Matching 25) ranking algorithm for text search.
    
    BM25 is a probabilistic ranking function that ranks documents based on
    query term frequency while accounting for document length normalization.
    
    Parameters:
        k1 (float): Controls term frequency saturation (default: 1.5)
        b (float): Controls document length normalization (default: 0.75)
    """
    
    def __init__(self, corpus: List[str], k1: float = 1.5, b: float = 0.75):
        """
        Initialize BM25 with a corpus of documents.
        
        Args:
            corpus: List of document strings
            k1: Term frequency saturation parameter
            b: Length normalization parameter
        """
        self.k1 = k1
        self.b = b
        self.corpus = corpus
        self.corpus_size = len(corpus)
        self.avgdl = 0
        self.doc_freqs = []
        self.idf = {}
        self.doc_len = []
        
        self._initialize()
    
    def _initialize(self):
        """Calculate document frequencies and IDF scores."""
        # Tokenize all documents
        tokenized_corpus = [self._tokenize(doc) for doc in self.corpus]
        
        # Calculate document lengths
        self.doc_len = [len(doc) for doc in tokenized_corpus]
        self.avgdl = sum(self.doc_len) / self.corpus_size if self.corpus_size > 0 else 0
        
        # Calculate document frequencies
        df = defaultdict(int)
        for doc_tokens in tokenized_corpus:
            unique_tokens = set(doc_tokens)
            for token in unique_tokens:
                df[token] += 1
        
        # Calculate IDF (Inverse Document Frequency)
        for token, freq in df.items():
            idf_score = math.log((self.corpus_size - freq + 0.5) / (freq + 0.5) + 1)
            self.idf[token] = idf_score
        
        # Store document word frequencies
        self.doc_freqs = [Counter(doc_tokens) for doc_tokens in tokenized_corpus]
    
    def _tokenize(self, text: str) -> List[str]:
        """
        Tokenize text into words.
        
        Args:
            text: Input text string
            
        Returns:
            List of lowercase tokens (words >= 3 characters)
        """
        # Convert to lowercase
        text = text.lower()
        
        # Remove punctuation and split
        text = re.sub(r'[^\w\s]', ' ', text)
        tokens = text.split()
        
        # Filter out short tokens
        tokens = [t for t in tokens if len(t) >= 3]
        
        return tokens
    
    def search(self, query: str, top_k: int = 10) -> List[Tuple[int, float]]:
        """
        Search for documents matching the query.
        
        Args:
            query: Search query string
            top_k: Number of top results to return
            
        Returns:
            List of (document_index, score) tuples, sorted by score descending
        """
        query_tokens = self._tokenize(query)
        
        # Calculate BM25 scores for all documents
        scores = []
        for doc_idx in range(self.corpus_size):
            score = self._calculate_score(query_tokens, doc_idx)
            if score > 0:  # Only include documents with positive scores
                scores.append((doc_idx, score))
        
        # Sort by score descending
        scores.sort(key=lambda x: x[1], reverse=True)
        
        return scores[:top_k]
    
    def _calculate_score(self, query_tokens: List[str], doc_idx: int) -> float:
        """
        Calculate BM25 score for a document given query tokens.
        
        Args:
            query_tokens: List of query tokens
            doc_idx: Document index
            
        Returns:
            BM25 score
        """
        score = 0.0
        doc_len = self.doc_len[doc_idx]
        doc_freqs = self.doc_freqs[doc_idx]
        
        for token in query_tokens:
            if token not in doc_freqs:
                continue
            
            # Get term frequency in document
            tf = doc_freqs[token]
            
            # Get IDF score
            idf = self.idf.get(token, 0)
            
            # Calculate BM25 component for this term
            numerator = tf * (self.k1 + 1)
            denominator = tf + self.k1 * (1 - self.b + self.b * (doc_len / self.avgdl))
            
            score += idf * (numerator / denominator)
        
        return score


class SEOSearchEngine:
    """
    SEO-specific search engine using BM25 ranking.
    
    Searches across multiple CSV knowledge bases for SEO rules and recommendations.
    """
    
    def __init__(self, data_dir: str):
        """
        Initialize SEO search engine.
        
        Args:
            data_dir: Directory containing CSV knowledge files
        """
        self.data_dir = data_dir
        self.indexes = {}
        self.data = {}
        
    def load_domain(self, domain: str, search_columns: List[str]) -> bool:
        """
        Load a knowledge domain from CSV file.
        
        Args:
            domain: Domain name (matches CSV filename without .csv)
            search_columns: List of column names to include in search index
            
        Returns:
            True if loaded successfully, False otherwise
        """
        csv_path = os.path.join(self.data_dir, f"{domain}.csv")
        
        if not os.path.exists(csv_path):
            return False
        
        # Load CSV data
        rows = []
        with open(csv_path, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                rows.append(row)
        
        # Build search corpus from specified columns
        corpus = []
        for row in rows:
            search_text = " ".join([
                str(row.get(col, "")) for col in search_columns if col in row
            ])
            corpus.append(search_text)
        
        # Create BM25 index
        self.indexes[domain] = BM25(corpus)
        self.data[domain] = rows
        
        return True
    
    def search(self, domain: str, query: str, max_results: int = 10) -> List[Dict]:
        """
        Search within a specific domain.
        
        Args:
            domain: Domain to search
            query: Search query
            max_results: Maximum number of results
            
        Returns:
            List of matching rows with scores
        """
        if domain not in self.indexes:
            return []
        
        # Get search results
        results = self.indexes[domain].search(query, top_k=max_results)
        
        # Return rows with scores
        output = []
        for doc_idx, score in results:
            row = self.data[domain][doc_idx].copy()
            row['_score'] = round(score, 2)
            row['_rank'] = len(output) + 1
            output.append(row)
        
        return output


def main():
    """Example usage of BM25 search engine."""
    # Example: Search technical SEO rules
    engine = SEOSearchEngine("./src/seo/data")
    
    # Load technical SEO domain
    engine.load_domain("technical-seo", ["Category", "Rule", "Description", "Keywords"])
    
    # Search for Core Web Vitals
    results = engine.search("technical-seo", "core web vitals performance", max_results=5)
    
    print("=== Search Results: Core Web Vitals ===\n")
    for result in results:
        print(f"Rank {result['_rank']}: {result['Rule']} (Score: {result['_score']})")
        print(f"Category: {result['Category']}")
        print(f"Description: {result['Description']}")
        print()


if __name__ == "__main__":
    main()
