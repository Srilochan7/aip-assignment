"""
Dataset Search Tool for Kaggle, HuggingFace, GitHub
"""

import requests
from crewai.tools import BaseTool
from typing import List, Dict

class DatasetSearchTool(BaseTool):
    name: str = "Dataset Search Tool"
    description: str = "Search relevant datasets on Kaggle, HuggingFace, GitHub."

    def _run(self, search_query: str) -> str:
        results = {
            "kaggle": self._search_kaggle(search_query),
            "huggingface": self._search_huggingface(search_query),
            "github": self._search_github(search_query)
        }
        return self._format(results, search_query)

    def _search_kaggle(self, query: str) -> List[Dict]:
        return [{
            "title": f"Kaggle datasets for {query}",
            "url": f"https://www.kaggle.com/datasets?q={query.replace(' ', '+')}",
            "description": f"Kaggle datasets relevant to {query}",
        }]

    def _search_huggingface(self, query: str) -> List[Dict]:
        url = f"https://huggingface.co/api/datasets?search={query}"
        resp = requests.get(url, timeout=10)
        datasets = []
        if resp.status_code == 200:
            for item in resp.json()[:5]:
                datasets.append({
                    "title": item.get("id", ""),
                    "url": f"https://huggingface.co/datasets/{item.get('id')}",
                    "description": item.get("description", "")
                })
        return datasets

    def _search_github(self, query: str) -> List[Dict]:
        url = "https://api.github.com/search/repositories"
        resp = requests.get(url, params={"q": f"{query} dataset", "sort": "stars"}, timeout=10)
        datasets = []
        if resp.status_code == 200:
            for item in resp.json().get("items", [])[:5]:
                datasets.append({
                    "title": item["name"],
                    "url": item["html_url"],
                    "description": item.get("description", "")})
        return datasets

    def _format(self, results: Dict, query: str) -> str:
        out = f"# Dataset Search Results for {query}\n\n"
        for platform, ds in results.items():
            out += f"## {platform.title()}\n"
            for item in ds:
                out += f"- [{item['title']}]({item['url']}): {item['description']}\n"
        return out

dataset_search_tool = DatasetSearchTool()