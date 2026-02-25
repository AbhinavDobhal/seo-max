#!/usr/bin/env python3
"""
Schema Validator for SEO Max

Detects, analyzes, and validates Schema.org markup (JSON-LD, Microdata, RDFa).
Generates missing schema implementation recommendations.

Features:
- Schema type detection and validation
- Required properties checking
- Data type validation
- Deprecation awareness (HowTo, FAQ, SpecialAnnouncement)
- Rich snippet eligibility assessment
- JSON-LD format optimization

Author: Abhinav Dobhal
License: MIT
"""

import json
import re
import sys
from collections import defaultdict
from typing import Dict, List, Tuple, Optional

# Local imports
from core import SEOSearchEngine


class SchemaValidator:
    """
    Comprehensive schema markup validator and generator.
    
    Supports 32+ schema types including:
    - Article, BlogPosting, NewsArticle
    - Product, AggregateOffer, Review
    - Organization, LocalBusiness, Person
    - VideoObject, BroadcastEvent, Clip
    - FAQ, HowTo, Event, Recipe
    - And 16+ more...
    """
    
    # Deprecated schema types (Google recommended)
    DEPRECATED_TYPES = {
        "HowTo": "2023-09",
        "FAQ": "2023-08",
        "SpecialAnnouncement": "2025-07"
    }
    
    # Restricted schema types
    RESTRICTED_TYPES = {
        "FAQ": ["gov", "health", "medical"]  # Only for government/health sites
    }
    
    # Required properties by schema type
    REQUIRED_PROPERTIES = {
        "Article": ["headline", "datePublished", "author", "image"],
        "BlogPosting": ["headline", "datePublished", "author", "image", "articleBody"],
        "NewsArticle": ["headline", "datePublished", "author", "image"],
        "Product": ["name", "description", "image", "brand", "offers"],
        "AggregateOffer": ["priceCurrency", "price", "availability"],
        "Review": ["reviewRating", "reviewBody", "author"],
        "Organization": ["name", "url", "logo"],
        "LocalBusiness": ["name", "address", "telephone"],
        "Event": ["name", "startDate", "location", "description"],
        "Recipe": ["name", "author", "prepTime", "cookTime", "recipeIngredient", "recipeInstructions"],
        "VideoObject": ["name", "description", "thumbnailUrl", "uploadDate", "duration"],
        "BroadcastEvent": ["name", "startDate", "url"],
        "FAQPage": ["mainEntity"],  # FAQ schema for pages
    }
    
    # Data type mappings
    DATA_TYPES = {
        "Text": ["str"],
        "URL": ["http://", "https://", "/"],
        "Date": ["ISO 8601", "YYYY-MM-DD"],
        "DateTime": ["ISO 8601", "YYYY-MM-DDTHH:MM:SS"],
        "Number": ["int", "float"],
        "Duration": ["PT"],  # ISO 8601 duration
        "ImageObject": ["url", "height", "width"],
        "Thing": ["name", "@id"],
    }
    
    def __init__(self, data_dir: str = "./src/seo/data"):
        """
        Initialize schema validator.
        
        Args:
            data_dir: Directory containing CSV knowledge files
        """
        self.data_dir = data_dir
        self.engine = SEOSearchEngine(data_dir)
        self.engine.load_domain(
            "schema-types",
            ["Type", "Description", "Status", "Keywords"]
        )
        
        # Load schema knowledge base
        self.schema_types = self._load_schema_database()
    
    def _load_schema_database(self) -> Dict[str, Dict]:
        """Load schema database from CSV."""
        schemas = {}
        if "schema-types" in self.engine.data:
            for row in self.engine.data["schema-types"]:
                type_name = row.get("Type", "")
                schemas[type_name] = {
                    "description": row.get("Description", ""),
                    "status": row.get("Status", "active"),
                    "keywords": row.get("Keywords", "")
                }
        return schemas
    
    def analyze(self, url: str, html_content: str) -> Dict:
        """
        Analyze schema markup in HTML content.
        
        Args:
            url: Page URL
            html_content: Raw HTML content
            
        Returns:
            Schema analysis report
        """
        # Extract all schema markup
        jsonld_schemas = self._extract_jsonld(html_content)
        microdata_schemas = self._extract_microdata(html_content)
        rdfa_schemas = self._extract_rdfa(html_content)
        
        all_schemas = []
        all_schemas.extend([(s, "JSON-LD") for s in jsonld_schemas])
        all_schemas.extend([(s, "Microdata") for s in microdata_schemas])
        all_schemas.extend([(s, "RDFa") for s in rdfa_schemas])
        
        # Validate each schema
        validations = []
        for schema_data, format_type in all_schemas:
            validation = self._validate_schema(schema_data, format_type, url)
            validations.append(validation)
        
        # Generate recommendations
        recommendations = self._generate_recommendations(url, validations)
        
        # Calculate health score
        health_score = self._calculate_health_score(validations)
        
        return {
            "url": url,
            "total_schemas_found": len(all_schemas),
            "health_score": health_score,
            "max_score": 100,
            "formats": {
                "json-ld": len(jsonld_schemas),
                "microdata": len(microdata_schemas),
                "rdfa": len(rdfa_schemas)
            },
            "schemas": validations,
            "recommendations": recommendations,
            "issues": self._collect_issues(validations),
            "opportunities": self._collect_opportunities(validations)
        }
    
    def _extract_jsonld(self, html_content: str) -> List[Dict]:
        """Extract JSON-LD schema blocks."""
        schemas = []
        pattern = r'<script[^>]*type=["\']application/ld\+json["\'][^>]*>(.*?)</script>'
        
        for match in re.finditer(pattern, html_content, re.DOTALL | re.IGNORECASE):
            try:
                schema_text = match.group(1).strip()
                # Handle multiple schemas in one block
                if schema_text.startswith('['):
                    schema_list = json.loads(schema_text)
                    schemas.extend(schema_list if isinstance(schema_list, list) else [schema_list])
                else:
                    schemas.append(json.loads(schema_text))
            except json.JSONDecodeError:
                schemas.append({
                    "@type": "Invalid JSON-LD",
                    "_raw": match.group(1)[:100] + "..."
                })
        
        return schemas
    
    def _extract_microdata(self, html_content: str) -> List[Dict]:
        """Extract Microdata schema attributes."""
        schemas = []
        
        # Find itemscope elements
        pattern = r'<[^>]*itemscope[^>]*itemtype=["\']([^"\']+)["\'][^>]*>'
        
        for match in re.finditer(pattern, html_content, re.IGNORECASE):
            schema_type = match.group(1).split('/')[-1]  # Get type from URL
            schemas.append({
                "@type": schema_type,
                "format": "Microdata",
                "_detected": True
            })
        
        return schemas
    
    def _extract_rdfa(self, html_content: str) -> List[Dict]:
        """Extract RDFa schema attributes."""
        schemas = []
        
        # Find RDFa typeof attributes
        pattern = r'typeof=["\']([^"\']+)["\']'
        
        found_types = set()
        for match in re.finditer(pattern, html_content, re.IGNORECASE):
            schema_type = match.group(1).split('/')[-1]
            if schema_type not in found_types:
                found_types.add(schema_type)
                schemas.append({
                    "@type": schema_type,
                    "format": "RDFa",
                    "_detected": True
                })
        
        return schemas
    
    def _validate_schema(self, schema: Dict, format_type: str, url: str) -> Dict:
        """
        Validate individual schema markup.
        
        Args:
            schema: Schema object (parsed or detected)
            format_type: JSON-LD, Microdata, or RDFa
            url: Page URL
            
        Returns:
            Validation report for this schema
        """
        validation = {
            "format": format_type,
            "type": schema.get("@type", "Unknown"),
            "valid": True,
            "issues": [],
            "warnings": [],
            "missing_properties": [],
            "data_type_errors": []
        }
        
        schema_type = validation["type"]
        
        # Check if type is deprecated
        if schema_type in self.DEPRECATED_TYPES:
            deprecation_date = self.DEPRECATED_TYPES[schema_type]
            validation["warnings"].append(
                f"{schema_type} is deprecated (as of {deprecation_date}). Consider alternative approaches."
            )
        
        # Check if type is restricted
        if schema_type in self.RESTRICTED_TYPES:
            restricted_domains = self.RESTRICTED_TYPES[schema_type]
            # Parse domain from URL
            domain_category = self._categorize_domain(url)
            if domain_category not in restricted_domains:
                validation["warnings"].append(
                    f"{schema_type} is restricted to: {', '.join(restricted_domains)}"
                )
        
        # Check required properties
        if schema_type in self.REQUIRED_PROPERTIES:
            required = self.REQUIRED_PROPERTIES[schema_type]
            for prop in required:
                if prop not in schema:
                    validation["missing_properties"].append(prop)
                    validation["valid"] = False
        
        # Validate data types for selected properties
        for key, value in schema.items():
            if key.startswith("@"):
                continue
            
            # Basic type validation
            if isinstance(value, str):
                if key in ["url", "image", "sameAs"] and not (value.startswith("http") or value.startswith("/")):
                    validation["data_type_errors"].append(f"{key}: Invalid URL format")
            elif isinstance(value, dict):
                # Nested object validation
                if "@type" in value:
                    nested_type = value["@type"]
                    if nested_type not in self.schema_types:
                        validation["warnings"].append(f"Unknown schema type: {nested_type}")
        
        # Check for placeholder text (common validation issue)
        for key, value in schema.items():
            if isinstance(value, str) and any(placeholder in value.lower() for placeholder in ["placeholder", "example", "your", "change this"]):
                validation["issues"].append(f"{key} contains placeholder text: '{value}'")
        
        return validation
    
    def _categorize_domain(self, url: str) -> str:
        """
        Categorize domain type (gov, health, commercial, etc).
        
        Args:
            url: Page URL
            
        Returns:
            Domain category
        """
        url_lower = url.lower()
        if ".gov" in url_lower:
            return "gov"
        if any(term in url_lower for term in ["health", "medical", "doctor", "hospital", "clinic"]):
            return "health"
        return "commercial"
    
    def _collect_issues(self, validations: List[Dict]) -> List[str]:
        """Collect all critical issues."""
        issues = []
        for val in validations:
            issues.extend(val["issues"])
            if not val["valid"]:
                issues.append(f"{val['type']}: Missing required properties: {', '.join(val['missing_properties'])}")
            issues.extend(val["data_type_errors"])
        return issues
    
    def _collect_opportunities(self, validations: List[Dict]) -> List[str]:
        """Collect schema implementation opportunities."""
        detected_types = {v["type"] for v in validations}
        
        opportunities = []
        
        # Common opportunities
        if "Article" not in detected_types and "BlogPosting" not in detected_types:
            opportunities.append("📝 Add Article or BlogPosting schema to content pages")
        
        if "Organization" not in detected_types:
            opportunities.append("🏢 Add Organization schema on homepage")
        
        if len(validations) == 0:
            opportunities.append("Add schema markup using JSON-LD (recommended format)")
        
        # Check for rich snippet eligibility
        if "Product" in detected_types:
            opportunities.append("✅ Product schema found - Enable product rich snippets")
        
        if "Recipe" in detected_types:
            opportunities.append("✅ Recipe schema found - Enable recipe rich snippets")
        
        if "Review" in detected_types:
            opportunities.append("✅ Review schema found - Enable review rich snippets")
        
        return opportunities
    
    def _calculate_health_score(self, validations: List[Dict]) -> int:
        """Calculate overall schema health score."""
        if not validations:
            return 0
        
        total_score = 0
        for val in validations:
            score = 100
            
            # Deduct for issues
            score -= len(val["issues"]) * 10
            score -= len(val["warnings"]) * 5
            score -= len(val["missing_properties"]) * 15
            score -= len(val["data_type_errors"]) * 10
            
            # Bonus for valid schemas
            if val["valid"]:
                score += 10
            
            total_score += max(0, score)
        
        avg_score = total_score // len(validations) if validations else 0
        return max(0, min(100, avg_score))
    
    def _generate_recommendations(self, url: str, validations: List[Dict]) -> List[str]:
        """
        Generate prioritized schema recommendations.
        
        Args:
            url: Page URL
            validations: List of schema validations
            
        Returns:
            List of recommendations
        """
        recommendations = []
        detected_types = {v["type"] for v in validations}
        
        # Priority 1: Fix invalid schemas
        for val in validations:
            if not val["valid"]:
                recommendations.append(
                    f"🔴 HIGH: Fix {val['type']} schema - missing properties: {', '.join(val['missing_properties'][:3])}"
                )
            
            if val["issues"]:
                recommendations.append(f"⚠️ MEDIUM: {val['type']} has issues - {val['issues'][0]}")
        
        # Priority 2: Add format recommendations
        if not any(v["format"] == "JSON-LD" for v in validations):
            recommendations.append("💡 Use JSON-LD format (recommended by Google) instead of Microdata/RDFa")
        
        # Priority 3: Add missing high-value schemas
        if not any(t in detected_types for t in ["Article", "BlogPosting", "NewsArticle"]):
            domain = self._categorize_domain(url)
            if "blog" in url or domain != "commercial":
                recommendations.append("📝 Add BlogPosting schema with author, publishedDate, and body")
        
        # Priority 4: Deprecation warnings
        for val in validations:
            if val["warnings"]:
                recommendations.append(f"⚠️ {val['type']}: {val['warnings'][0]}")
        
        return recommendations[:10]  # Top 10 recommendations


def main():
    """Example usage."""
    if len(sys.argv) < 2:
        print("Usage: python schema_validator.py <url> [html_file]")
        sys.exit(1)
    
    url = sys.argv[1]
    
    # Sample HTML with schema
    sample_html = """
    <html>
    <head>
        <script type="application/ld+json">
        {
          "@context": "https://schema.org",
          "@type": "BlogPosting",
          "headline": "The Complete SEO Guide for 2026",
          "datePublished": "2026-02-25",
          "author": {
            "@type": "Person",
            "name": "SEO Expert"
          },
          "image": "https://example.com/seo-guide.jpg",
          "articleBody": "Comprehensive guide..."
        }
        </script>
    </head>
    <body>
        <h1>The Complete SEO Guide for 2026</h1>
    </body>
    </html>
    """
    
    validator = SchemaValidator()
    result = validator.analyze(url, sample_html)
    
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
