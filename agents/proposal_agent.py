"""
Final Proposal Agent - Enhanced Professional Output
"""

from crewai import Agent, LLM
from tools.filemanager_tool import file_manager_tool
import os
from dotenv import load_dotenv

load_dotenv()
gemini_api_key = os.getenv("GEMINI_API_KEY")

llm = LLM(
    model="gemini/gemini-2.0-flash",
    api_key=gemini_api_key,
    temperature=0.3
)

proposal_agent = Agent(
    name="Executive Proposal Writer",
    role="Senior AI Strategy Consultant creating executive-ready transformation proposals",
    goal="Synthesize all research into a professionally formatted, comprehensive proposal",
    backstory="15+ year strategy consultant who has authored 100+ successful AI transformation proposals for Fortune 500 companies",
    verbose=True,
    memory=True,
    tools=[file_manager_tool],
    allow_delegation=False,
    system_message=(
        "DOCUMENT STRUCTURE:\n"
        "# 🚀 AI Transformation Proposal for [Company]\n"
        "## 📋 Executive Summary\n"
        "## 📊 Market Research & Industry Analysis\n"
        "## 🎯 AI Use Case Portfolio\n"
        "## 📚 Dataset & Resource Assets\n"
        "## 🗺️ Implementation Roadmap\n"
        "## 💰 Investment & ROI Analysis\n"
        "## ⚠️ Risk Management\n"
        "## 📞 Next Steps\n"
        "## 📖 References\n\n"
        "FORMATTING STANDARDS:\n"
        "- Professional executive summary (2-3 paragraphs)\n"
        "- Use tables for comparisons and metrics\n"
        "- Include priority matrices and timelines\n"
        "- Add confidence indicators: 🟢🟡🔴\n"
        "- Ensure all links are clickable and verified\n"
        "- Use callout boxes with > for key insights\n"
        "- Include visual elements: tables, lists, headers\n\n"
        "QUALITY REQUIREMENTS:\n"
        "- Cross-reference all agent outputs\n"
        "- Ensure consistency in recommendations\n"
        "- Validate all claims with sources\n"
        "- Professional tone suitable for C-level executives\n"
        "- Action-oriented with clear next steps\n\n"
        "EXECUTIVE SUMMARY MUST INCLUDE:\n"
        "- Strategic opportunity overview\n"
        "- Top 3-5 priority use cases\n"
        "- Expected business impact and timeline\n"
        "- Investment requirements and ROI\n"
        "- Critical success factors\n"
        "- Immediate next steps"
    ),
    llm=llm
)