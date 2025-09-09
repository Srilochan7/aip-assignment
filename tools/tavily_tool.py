from crewai import tools
from crewai_tools import TavilySearchTool

import os

from dotenv import load_dotenv
load_dotenv()


class TavilyTool:
    
    
    def __init__(self):
        self.api_key = os.getenv("TAVILY_API_KEY")
        if not self.api_key:
            raise ValueError("TAVILY_API_KEY environment variable not set.")
        
        self.tool = TavilySearchTool(
            api_key=self.api_key,
            search_depth="advanced",
            max_results=5,
            include_raw_content=False,
            include_images=False
        )
        
        
        
    def search_industry_data(self, query: str) -> str:
        """Search for industry-specific data and trends"""
        enhanced_query = f"industry analysis trends market research {query} 2024"
        return self.tool.run(enhanced_query)
    
    def search_ai_use_cases(self, industry: str) -> str:
        """Search for AI/ML use cases in specific industry"""
        query = f"AI machine learning generative AI use cases applications {industry} industry 2024"
        return self.tool.run(query)
    
    def search_competitor_analysis(self, company: str, industry: str) -> str:
        """Search for competitor analysis and market position"""
        query = f"{company} competitors market analysis {industry} industry positioning"
        return self.tool.run(query)
    
    
    
tavily = TavilyTool().tool