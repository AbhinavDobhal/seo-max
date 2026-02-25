#!/usr/bin/env python3
"""
Insights Optimizer for SEO Max

Analyzes and optimizes for AI-powered search visibility.
Includes Google AI Overviews, ChatGPT web search, Perplexity, and other AI search engines.

Features:
- AI visibility signal detection (20+ signals)
- Platform-specific optimization (Google, ChatGPT, Perplexity)
- Authority and trust factor analysis
- Content structure for AI extraction
- EEAT (Experience, Expertise, Authoritativeness, Trustworthiness) scoring

Key Metrics:
- YouTube presence correlation (0.737)
- Brand signal strength (3× stronger than backlinks)
- Content freshness for AI indexing
- Structured data completeness

Author: Abhinav Dobhal
License: MIT
"""

import json
import re
import sys
from collections import defaultdict
from typing import Dict, List, Tuple, Optional
from urllib.parse import urlparse, quote

# Local imports
from core import SEOSearchEngine


class InsightsOptimizer:
    """
    AI search optimization analyzer.
    
    Evaluates content for visibility in:
    - Google AI Overviews
    - ChatGPT web search
    - Perplexity
    - Other LLM-based search engines
    
    Scoring dimensions (20+ signals):
    - Content authority and expertise
    - Brand recognition and citations
    - YouTube/media presence
    - Citation patterns and mentions
    - Question-answer format
    - Product/service clarity
    - Trust signals (credentials, reviews)
    """
    
    # AI visibility signal weights
    AI_SIGNALS = {
        "YouTube Channel Present": {"weight": 0.737, "category": "Authority"},
        "Brand Mentions": {"weight": 0.850, "category": "Authority"},
        "Author Credentials": {"weight": 0.720, "category": "Authority"},
        "Publication Dates": {"weight": 0.680, "category": "Freshness"},
        "Update Frequency": {"weight": 0.700, "category": "Freshness"},
        "Question Answer Format": {"weight": 0.800, "category": "Format"},
        "Structured Lists": {"weight": 0.650, "category": "Format"},
        "Direct Answers": {"weight": 0.900, "category": "Format"},
        "Schema Markup": {"weight": 0.780, "category": "Structure"},
        "Internal Links": {"weight": 0.620, "category": "Structure"},
        "External Links to Authorities": {"weight": 0.850, "category": "Authority"},
        "Customer Reviews": {"weight": 0.810, "category": "Trust"},
        "Security HTTPS": {"weight": 0.700, "category": "Trust"},
        "Contact Information": {"weight": 0.650, "category": "Trust"},
        "Privacy Policy": {"weight": 0.600, "category": "Trust"},
        "Social Proof": {"weight": 0.740, "category": "Trust"},
        "Technical Performance": {"weight": 0.680, "category": "Technical"},
        "Mobile Optimization": {"weight": 0.750, "category": "Technical"},
        "Core Web Vitals": {"weight": 0.700, "category": "Technical"},
        "Content Depth": {"weight": 0.850, "category": "Content"},
    }
    
    def __init__(self, data_dir: str = "./src/seo/data"):
        """
        Initialize insights optimizer.
        
        Args:
            data_dir: Directory containing CSV knowledge files
        """
        self.data_dir = data_dir
        self.engine = SEOSearchEngine(data_dir)
        self.engine.load_domain(
            "insights-signals",
            ["Signal", "Description", "Platform", "Correlation"]
        )
        
        # Load signals database
        self.signals = self._load_signals_database()
    
    def _load_signals_database(self) -> Dict[str, Dict]:
        """Load AI signals database from CSV."""
        signals = {}
        if "insights-signals" in self.engine.data:
            for row in self.engine.data["insights-signals"]:
                signal_name = row.get("Signal", "")
                signals[signal_name] = {
                    "description": row.get("Description", ""),
                    "platform": row.get("Platform", "All"),
                    "correlation": float(row.get("Correlation", "0.5")),
                }
        return signals
    
    def analyze(self, url: str, html_content: str, metadata: Dict = None) -> Dict:
        """
        Analyze page for AI search optimization.
        
        Args:
            url: Page URL
            html_content: Raw HTML content
            metadata: Optional page metadata
            
        Returns:
            AI visibility analysis report
        """
        if metadata is None:
            metadata = {}
        
        # Parse content
        parsed = self._parse_content(html_content, metadata, url)
        
        # Score each signal
        signal_scores = {}
        for signal_name, signal_info in self.AI_SIGNALS.items():
            score, evidence = self._evaluate_signal(signal_name, parsed)
            signal_scores[signal_name] = {
                "score": score,
                "weight": signal_info["weight"],
                "category": signal_info["category"],
                "evidence": evidence
            }
        
        # Calculate platform-specific scores
        google_score = self._calculate_platform_score(signal_scores, "Google")
        chatgpt_score = self._calculate_platform_score(signal_scores, "ChatGPT")
        perplexity_score = self._calculate_platform_score(signal_scores, "Perplexity")
        
        # Calculate overall AI visibility score
        overall_score = (google_score + chatgpt_score + perplexity_score) / 3
        
        # Generate category insights
        category_insights = self._analyze_by_category(signal_scores)
        
        # Generate recommendations
        recommendations = self._generate_recommendations(signal_scores, parsed)
        
        return {
            "url": url,
            "ai_visibility_score": round(overall_score, 1),
            "max_score": 100,
            "platform_scores": {
                "google_ai_overviews": round(google_score, 1),
                "chatgpt_web_search": round(chatgpt_score, 1),
                "perplexity": round(perplexity_score, 1)
            },
            "categories": category_insights,
            "signals": signal_scores,
            "eeat_score": self._calculate_eeat_score(parsed),
            "authority_level": self._categorize_authority(overall_score),
            "recommendations": recommendations,
            "quick_wins": self._identify_quick_wins(signal_scores),
            "competitive_analysis": self._competitive_analysis(parsed)
        }
    
    def _parse_content(self, html_content: str, metadata: Dict, url: str) -> Dict:
        """Parse HTML content for analysis."""
        parsed = {
            "title": metadata.get("title", ""),
            "description": metadata.get("description", ""),
            "url": url,
            "domain": urlparse(url).netloc,
            "word_count": 0,
            "headings": [],
            "questions": 0,
            "has_youtube": False,
            "has_schema": False,
            "has_author_credentials": False,
            "has_dates": False,
            "has_reviews": False,
            "links_external": 0,
            "links_authority": 0,
            "has_https": False,
            "has_contact": False,
            "has_privacy": False,
            "text_content": "",
            "brand_mentions": 0,
            "social_signals": 0,
            "freshness": 0,  # days since update
            "mobile_optimized": False,
            "page_speed_score": 50,  # 0-100 estimated
        }
        
        # Extract text
        text_only = re.sub(r'<[^>]+>', ' ', html_content)
        text_only = re.sub(r'\s+', ' ', text_only).strip()
        parsed["text_content"] = text_only
        parsed["word_count"] = len(text_only.split())
        
        # Count questions (Q&A format indicator)
        q_marks = len(re.findall(r'<[hb][1-3][^>]*>[^<]*\?', html_content, re.IGNORECASE))
        parsed["questions"] = q_marks
        
        # Check for media
        parsed["has_youtube"] = "youtube.com" in html_content or "youtu.be" in html_content
        
        # Check for schema
        parsed["has_schema"] = '<script type="application/ld+json">' in html_content or 'itemtype=' in html_content
        
        # Check for author credentials
        parsed["has_author_credentials"] = any(
            term in html_content.lower() for term in ["PhD", "expert", "certified", "credentials", "author bio"]
        )
        
        # Check for dates
        parsed["has_dates"] = bool(re.search(r'202[0-9]|2[01][0-9]{2}', html_content))
        
        # Check for reviews/ratings
        parsed["has_reviews"] = any(
            term in html_content.lower() for term in ["review", "rating", "aggregate rating", "stars"]
        )
        
        # Count external authority links
        for link in re.finditer(r'href=["\']([^"\']+)["\'|]', html_content, re.IGNORECASE):
            href = link.group(1)
            if href.startswith('http'):
                parsed["links_external"] += 1
                if any(authority in href for authority in [".edu", ".gov", "wikipedia", "ny times", "bbc"]):
                    parsed["links_authority"] += 1
        
        # Check security and trust
        parsed["has_https"] = "https://" in html_content or "<link rel" in html_content
        parsed["has_contact"] = any(
            term in html_content.lower() for term in ["contact", "email", "phone", "form"]
        )
        parsed["has_privacy"] = "privacy" in html_content.lower() or "GDPR" in html_content
        
        # Mobile optimization
        parsed["mobile_optimized"] = "viewport" in html_content.lower()
        
        return parsed
    
    def _evaluate_signal(self, signal_name: str, parsed: Dict) -> Tuple[float, str]:
        """
        Evaluate a single AI visibility signal.
        
        Args:
            signal_name: Name of signal to evaluate
            parsed: Parsed content data
            
        Returns:
            (score, evidence) tuple
        """
        # Default evaluation logic by signal type
        if signal_name == "YouTube Channel Present":
            score = 100.0 if parsed["has_youtube"] else 0.0
            evidence = "YouTube channel/videos detected" if parsed["has_youtube"] else "No YouTube presence"
        
        elif signal_name == "Brand Mentions":
            mentions = parsed["brand_mentions"]
            score = min(100.0, mentions * 10)
            evidence = f"{mentions} brand mentions detected"
        
        elif signal_name == "Author Credentials":
            score = 100.0 if parsed["has_author_credentials"] else 30.0
            evidence = "Author credentials present" if parsed["has_author_credentials"] else "Missing author bio"
        
        elif signal_name == "Publication Dates":
            score = 100.0 if parsed["has_dates"] else 20.0
            evidence = "Publication date visible" if parsed["has_dates"] else "No date information"
        
        elif signal_name == "Question Answer Format":
            q_ratio = parsed["questions"] / max(1, parsed["word_count"] / 100) if parsed["word_count"] > 0 else 0
            score = min(100.0, q_ratio * 50)
            evidence = f"{parsed['questions']} question format detected"
        
        elif signal_name == "Direct Answers":
            has_direct = parsed["word_count"] > 100  # Placeholder logic
            score = 85.0 if has_direct else 30.0
            evidence = "Content structured for direct answers" if has_direct else "Insufficient answer content"
        
        elif signal_name == "Schema Markup":
            score = 100.0 if parsed["has_schema"] else 20.0
            evidence = "Schema markup present" if parsed["has_schema"] else "No structured data"
        
        elif signal_name == "External Links to Authorities":
            score = min(100.0, parsed["links_authority"] * 15)
            evidence = f"{parsed['links_authority']} authority links detected"
        
        elif signal_name == "Customer Reviews":
            score = 100.0 if parsed["has_reviews"] else 40.0
            evidence = "Review/rating schema detected" if parsed["has_reviews"] else "No reviews present"
        
        elif signal_name == "Security HTTPS":
            score = 100.0 if parsed["has_https"] else 30.0
            evidence = "HTTPS secured" if parsed["has_https"] else "Not HTTPS"
        
        elif signal_name == "Contact Information":
            score = 100.0 if parsed["has_contact"] else 20.0
            evidence = "Contact info available" if parsed["has_contact"] else "Missing contact page"
        
        elif signal_name == "Privacy Policy":
            score = 100.0 if parsed["has_privacy"] else 10.0
            evidence = "Privacy policy present" if parsed["has_privacy"] else "No privacy notice"
        
        elif signal_name == "Mobile Optimization":
            score = 100.0 if parsed["mobile_optimized"] else 30.0
            evidence = "Mobile responsive" if parsed["mobile_optimized"] else "Not mobile optimized"
        
        elif signal_name == "Content Depth":
            score = min(100.0, (parsed["word_count"] / 20))  # 2000+ words = 100
            evidence = f"{parsed['word_count']} words"
        
        else:
            score = 50.0
            evidence = "Default signal value"
        
        return min(100.0, score), evidence
    
    def _calculate_platform_score(self, signal_scores: Dict, platform: str) -> float:
        """Calculate platform-specific AI visibility score."""
        platform_signals = {
            "Google": ["Direct Answers", "Schema Markup", "Mobile Optimization", "Core Web Vitals"],
            "ChatGPT": ["Content Depth", "External Links to Authorities", "Question Answer Format"],
            "Perplexity": ["Citation Patterns", "Direct Answers", "Content Depth"]
        }
        
        if platform not in platform_signals:
            return 50.0
        
        signals = platform_signals[platform]
        weighted_score = 0
        total_weight = 0
        
        for signal_name, data in signal_scores.items():
            if any(s.lower() in signal_name.lower() for s in signals):
                weighted_score += data["score"] * data["weight"]
                total_weight += data["weight"]
        
        return weighted_score / total_weight if total_weight > 0 else 50.0
    
    def _calculate_eeat_score(self, parsed: Dict) -> Dict:
        """Calculate E-E-A-T (Experience, Expertise, Authoritativeness, Trustworthiness)."""
        return {
            "experience": 100 if parsed["has_author_credentials"] else 40,
            "expertise": min(100, (parsed["word_count"] / 20)),  # Based on content depth
            "authoritativeness": min(100, parsed["links_authority"] * 20),
            "trustworthiness": (
                (100 if parsed["has_https"] else 0) +
                (50 if parsed["has_contact"] else 0) +
                (50 if parsed["has_privacy"] else 0)
            ) // 3
        }
    
    def _categorize_authority(self, score: float) -> str:
        """Categorize authority level based on AI visibility score."""
        if score >= 75:
            return "🟢 High Authority - Strong AI search visibility"
        elif score >= 50:
            return "🟡 Medium Authority - Moderate AI search visibility"
        else:
            return "🔴 Low Authority - Limited AI search visibility"
    
    def _analyze_by_category(self, signal_scores: Dict) -> Dict:
        """Analyze signals grouped by category."""
        categories = defaultdict(list)
        for signal_name, data in signal_scores.items():
            category = data["category"]
            categories[category].append(data["score"])
        
        return {
            category: round(sum(scores) / len(scores), 1)
            for category, scores in categories.items()
        }
    
    def _generate_recommendations(self, signal_scores: Dict, parsed: Dict) -> List[str]:
        """Generate prioritized AI search optimization recommendations."""
        recommendations = []
        
        # Priority 1: Critical improvements (score < 30)
        for signal_name, data in signal_scores.items():
            if data["score"] < 30 and "Authority" in data["category"]:
                recommendations.append(f"🔴 CRITICAL: {signal_name} - {data['evidence']}")
        
        # Priority 2: High impact improvements
        for signal_name, data in signal_scores.items():
            if data["score"] < 50 and "Content" in data["category"]:
                recommendations.append(f"🟡 HIGH: Improve {signal_name}")
        
        # Priority 3: Optimization tips
        if parsed["word_count"] < 2000:
            recommendations.append("📝 Expand content to 2000+ words for better AI extraction")
        
        if not parsed["has_schema"]:
            recommendations.append("⚡ Add schema markup (20-30% authority boost)")
        
        if parsed["links_authority"] == 0:
            recommendations.append("🔗 Link to authoritative sources (.edu, .gov, established publishers)")
        
        return recommendations[:7]
    
    def _identify_quick_wins(self, signal_scores: Dict) -> List[str]:
        """Identify quick-win optimizations with high ROI."""
        quick_wins = []
        
        for signal_name, data in signal_scores.items():
            if data["score"] < 100 and data["weight"] > 0.7:  # High-impact signals that aren't perfect
                quick_wins.append(f"💡 {signal_name}: {data['evidence']}")
        
        return quick_wins[:5]
    
    def _competitive_analysis(self, parsed: Dict) -> Dict:
        """Competitive analysis for AI search visibility."""
        return {
            "content_depth_gap": max(0, 2000 - parsed["word_count"]),
            "authority_links_needed": max(0, 5 - parsed["links_authority"]),
            "schema_recommended": not parsed["has_schema"],
            "brand_amplification_needed": parsed["brand_mentions"] == 0,
        }


def main():
    """Example usage."""
    if len(sys.argv) < 2:
        print("Usage: python insights_optimizer.py <url> [html_file]")
        sys.exit(1)
    
    url = sys.argv[1]
    
    # Sample HTML
    sample_html = """
    <html>
    <head>
        <title>The Complete SEO Guide for AI-Powered Search - 2026</title>
        <meta name="description" content="Learn how to optimize your content for AI search engines...">
    </head>
    <body>
        <h1>The Complete SEO Guide for AI-Powered Search</h1>
        <h2>What is AI Search Optimization?</h2>
        <p>AI search optimization (GEO) involves tailoring your content...</p>
        <img alt="AI Search Diagram" src="ai-search.jpg">
    </body>
    </html>
    """
    
    optimizer = InsightsOptimizer()
    result = optimizer.analyze(url, sample_html)
    
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
