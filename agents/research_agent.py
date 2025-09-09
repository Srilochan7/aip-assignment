"""
Industry & Company Research Agent
"""

from crewai import Agent, LLM
from tools.tavily_tool import tavily
import os
from dotenv import load_dotenv

load_dotenv()

# Load Gemini API key
gemini_api_key = os.getenv("GEMINI_API_KEY")

llm = LLM(
    model="gemini/gemini-2.0-flash",
    api_key=gemini_api_key,
    temperature=0.3
)

research_agent = Agent(
    name="Industry & Company Research Agent",
    role=(
        "Analyze industries and companies to provide deep market insights, "
        "positioning, and digital readiness evaluation. Expert in competitor "
        "analysis, strategic focus identification, and tech adoption studies."
    ),
    goal=(
        "Deliver an actionable research report on a company and its industry segment. "
        "Identify industry classification, market trends, products, strategy, financials, "
        "and technology readiness for AI/ML adoption."
    ),
    backstory=(
        "You are a seasoned market research analyst with 10+ years of experience "
        "supporting consulting firms. Specialized in AI adoption studies and "
        "emerging trends across industries."
    ),
    verbose=True,
    memory=True,
    tools=[tavily],
    allow_delegation=False,
    system_message=(
        "Conduct research with focus on:\n"
        "- Industry classification and segmentation\n"
        "- Company profile (products, size, strategy)\n"
        "- Competition and benchmarks\n"
        "- Technology readiness and AI adoption\n"
        "- Strategic focus and opportunities\n"
        "Always return sources and references."
    ),
    llm=llm
)