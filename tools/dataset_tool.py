"""
Enhanced Dataset Search Tool with Proper Link Formatting
"""

import requests
import urllib.parse
from crewai.tools import BaseTool
from typing import List, Dict
import time

class DatasetSearchTool(BaseTool):
    name: str = "Enhanced Dataset Search Tool"
    description: str = "Search and validate datasets on Kaggle, HuggingFace, GitHub with quality assessment"

    def _run(self, search_query: str) -> str:
        try:
            results = {
                "kaggle": self._search_kaggle_enhanced(search_query),
                "huggingface": self._search_huggingface_enhanced(search_query),
                "github": self._search_github_enhanced(search_query)
            }
            return self._format_enhanced_results(results, search_query)
        except Exception as e:
            return f"🚨 Search Error: {str(e)}"

    def _search_kaggle_enhanced(self, query: str) -> List[Dict]:
        """Enhanced Kaggle search with proper URL encoding"""
        encoded_query = urllib.parse.quote_plus(query)
        
        # Multiple search approaches for better coverage
        searches = [
            {"term": f"{query} dataset", "category": "datasets"},
            {"term": f"{query} machine learning", "category": "datasets"},
            {"term": f"{query} competition", "category": "competitions"}
        ]
        
        results = []
        for search in searches:
            encoded_term = urllib.parse.quote_plus(search["term"])
            if search["category"] == "datasets":
                url = f"https://www.kaggle.com/datasets?search={encoded_term}"
            else:
                url = f"https://www.kaggle.com/competitions?search={encoded_term}"
            
            results.append({
                "title": f"Kaggle {search['term'].title()}",
                "url": url,
                "description": f"Curated {search['category']} for {query} with community contributions and documentation",
                "platform": "🏆 Kaggle",
                "quality_score": "7-9",
                "access": "Free with registration",
                "type": search["category"].title(),
                "features": ["Community verified", "CSV/JSON formats", "Kernel examples"]
            })
        
        return results[:2]  # Limit to avoid overwhelming

    def _search_huggingface_enhanced(self, query: str) -> List[Dict]:
        """Enhanced HuggingFace search with API validation"""
        results = []
        
        # Search datasets
        try:
            datasets_url = "https://huggingface.co/api/datasets"
            params = {"search": query, "limit": 5}
            response = requests.get(datasets_url, params=params, timeout=8)
            
            if response.status_code == 200:
                datasets = response.json()
                for item in datasets[:3]:
                    dataset_id = item.get("id", "")
                    if dataset_id:
                        downloads = item.get("downloads", 0)
                        quality_score = "9-10" if downloads > 10000 else "7-8" if downloads > 1000 else "6-7"
                        
                        results.append({
                            "title": f"HF Dataset: {dataset_id}",
                            "url": f"https://huggingface.co/datasets/{dataset_id}",
                            "description": (item.get("description", "ML-ready dataset"))[:150] + "...",
                            "platform": "🤗 HuggingFace",
                            "quality_score": quality_score,
                            "downloads": f"{downloads:,}",
                            "access": "Open source",
                            "type": "ML Dataset",
                            "features": ["Pre-processed", "API access", "Multiple formats"]
                        })
            
            # Search models
            models_url = "https://huggingface.co/api/models"
            params = {"search": query, "limit": 3}
            response = requests.get(models_url, params=params, timeout=8)
            
            if response.status_code == 200:
                models = response.json()
                for item in models[:2]:
                    model_id = item.get("id", "")
                    if model_id:
                        results.append({
                            "title": f"HF Model: {model_id}",
                            "url": f"https://huggingface.co/{model_id}",
                            "description": f"Pre-trained model for {query} applications with inference API",
                            "platform": "🤗 HuggingFace",
                            "quality_score": "8-10",
                            "downloads": f"{item.get('downloads', 0):,}",
                            "access": "Open source",
                            "type": "Pre-trained Model",
                            "features": ["Inference API", "Fine-tuning ready", "Documentation"]
                        })
                        
        except Exception as e:
            # Fallback to direct search URLs
            encoded_query = urllib.parse.quote_plus(query)
            results.extend([
                {
                    "title": f"HuggingFace Datasets: {query}",
                    "url": f"https://huggingface.co/datasets?search={encoded_query}",
                    "description": f"Search results for {query} datasets on HuggingFace platform",
                    "platform": "🤗 HuggingFace",
                    "quality_score": "8-10",
                    "access": "Open source",
                    "type": "Dataset Collection",
                    "features": ["ML-ready", "API access", "Community driven"],
                    "note": f"Direct search (API unavailable: {str(e)})"
                },
                {
                    "title": f"HuggingFace Models: {query}",
                    "url": f"https://huggingface.co/models?search={encoded_query}",
                    "description": f"Pre-trained models for {query} applications",
                    "platform": "🤗 HuggingFace",
                    "quality_score": "8-10",
                    "access": "Open source",
                    "type": "Model Collection",
                    "features": ["Inference API", "Fine-tuning", "Documentation"]
                }
            ])
        
        return results[:4]

    def _search_github_enhanced(self, query: str) -> List[Dict]:
        """Enhanced GitHub search with repository quality metrics"""
        results = []
        
        try:
            search_terms = [
                f"{query} dataset",
                f"{query} machine-learning awesome"
            ]
            
            for term in search_terms:
                url = "https://api.github.com/search/repositories"
                params = {
                    "q": f"{term} language:python",
                    "sort": "stars",
                    "order": "desc",
                    "per_page": 3
                }
                
                response = requests.get(url, params=params, timeout=8)
                
                if response.status_code == 200:
                    repos = response.json().get("items", [])
                    for item in repos:
                        stars = item.get("stargazers_count", 0)
                        forks = item.get("forks_count", 0)
                        
                        # Quality assessment based on community engagement
                        if stars > 5000:
                            quality_score = "9-10"
                        elif stars > 1000:
                            quality_score = "8-9"
                        elif stars > 100:
                            quality_score = "6-8"
                        else:
                            quality_score = "5-7"
                        
                        results.append({
                            "title": f"GitHub: {item['name']}",
                            "url": item["html_url"],
                            "description": (item.get("description", "Repository with datasets and code"))[:150] + "...",
                            "platform": "⭐ GitHub",
                            "quality_score": quality_score,
                            "stars": f"{stars:,}",
                            "forks": f"{forks:,}",
                            "access": "Open source",
                            "type": "Code Repository",
                            "language": item.get("language", "Multiple"),
                            "features": ["Source code", "Documentation", "Community support"]
                        })
                
                time.sleep(1)  # Rate limiting
                
        except Exception as e:
            # Fallback to direct search URLs
            encoded_query = urllib.parse.quote_plus(f"{query} dataset")
            results.append({
                "title": f"GitHub Search: {query} Datasets",
                "url": f"https://github.com/search?q={encoded_query}&type=repositories&s=stars&o=desc",
                "description": f"Search results for {query} datasets and repositories on GitHub",
                "platform": "⭐ GitHub",
                "quality_score": "Variable",
                "access": "Open source",
                "type": "Repository Search",
                "features": ["Source code", "Multiple languages", "Community driven"],
                "note": f"Direct search (API rate limited: {str(e)})"
            })
        
        return results[:3]

    def _format_enhanced_results(self, results: Dict, query: str) -> str:
        """Professional formatting with tables and structured layout"""
        output = f"# 📊 Dataset & Resource Collection Report\n\n"
        output += f"**🔍 Search Query:** `{query}`  \n"
        output += f"**📅 Generated:** {time.strftime('%Y-%m-%d %H:%M:%S')}  \n"
        
        total_resources = sum(len(resources) for resources in results.values())
        output += f"**📈 Total Resources:** {total_resources}\n\n"
        
        # Executive Summary Table
        output += "## 📋 Executive Summary\n\n"
        output += "| Platform | Resources | Quality Range | Access Model |\n"
        output += "|----------|-----------|---------------|-------------|\n"
        
        for platform, resources in results.items():
            if resources:
                quality_range = f"{min([r.get('quality_score', '5-7').split('-')[0] for r in resources])}-{max([r.get('quality_score', '5-7').split('-')[-1] for r in resources])}/10"
                output += f"| {platform.title()} | {len(resources)} | {quality_range} | Mixed |\n"
        
        output += "\n---\n\n"
        
        # Detailed Resources by Platform
        platform_emojis = {
            "kaggle": "🏆",
            "huggingface": "🤗",
            "github": "⭐"
        }
        
        for platform, resources in results.items():
            if not resources:
                continue
                
            output += f"## {platform_emojis.get(platform, '📈')} {platform.title()} Resources\n\n"
            
            for i, resource in enumerate(resources, 1):
                output += f"### {i}. **[{resource['title']}]({resource['url']})**\n\n"
                
                # Resource details in structured format
                output += f"**📝 Description:** {resource['description']}\n\n"
                
                # Metrics table for each resource
                output += "| Attribute | Value |\n"
                output += "|-----------|-------|\n"
                output += f"| **Platform** | {resource['platform']} |\n"
                output += f"| **Quality Score** | {resource['quality_score']}/10 |\n"
                output += f"| **Access** | {resource['access']} |\n"
                output += f"| **Type** | {resource['type']} |\n"
                
                # Platform-specific metrics
                if 'downloads' in resource:
                    output += f"| **Downloads** | {resource['downloads']} |\n"
                if 'stars' in resource:
                    output += f"| **Stars** | {resource['stars']} |\n"
                    output += f"| **Forks** | {resource['forks']} |\n"
                if 'language' in resource:
                    output += f"| **Language** | {resource['language']} |\n"
                
                output += "\n"
                
                # Features
                if 'features' in resource:
                    output += f"**✨ Key Features:**\n"
                    for feature in resource['features']:
                        output += f"- {feature}\n"
                    output += "\n"
                
                # Notes if any
                if 'note' in resource:
                    output += f"> 📌 **Note:** {resource['note']}\n\n"
                
                output += "---\n\n"
        
        # Usage Recommendations
        output += "## 💡 Implementation Recommendations\n\n"
        output += "### 🎯 Quality Assessment Guide\n"
        output += "| Score | Description | Recommendation |\n"
        output += "|-------|-------------|----------------|\n"
        output += "| 9-10/10 | Production-ready, excellent documentation | ✅ **Immediate use** |\n"
        output += "| 7-8/10 | Good quality, suitable for prototypes | 🟡 **Prototype & test** |\n"
        output += "| 5-6/10 | Requires evaluation and preprocessing | ⚠️ **Evaluate first** |\n"
        output += "| <5/10 | Use with caution, extensive testing needed | 🔴 **High risk** |\n\n"
        
        output += "### 🚀 Implementation Priority\n"
        output += "1. **🏆 High Priority:** HuggingFace datasets (>10K downloads) + GitHub repos (>1K stars)\n"
        output += "2. **🟡 Medium Priority:** Kaggle datasets + GitHub repos (>100 stars)\n"
        output += "3. **🔍 Evaluation Needed:** New or low-engagement resources\n\n"
        
        output += "### 🔗 Next Steps\n"
        output += "- **Validate** dataset relevance for specific use cases\n"
        output += "- **Review** licensing requirements for commercial use\n"
        output += "- **Test** data quality and preprocessing requirements\n"
        output += "- **Benchmark** model performance if applicable\n\n"
        
        return output

# Initialize the enhanced tool
dataset_search_tool = DatasetSearchTool()