"""
Final Proposal Agent
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
    temperature=0.35
)

proposal_agent = Agent(
    name="Final Proposal Agent",
    role=(
        "Senior AI Strategy Consultant responsible for producing executive-level "
        "AI/GenAI proposal reports."
    ),
    goal=(
        "Generate a comprehensive, C‑level presentation‑style proposal: industry insights, "
        "AI use cases, datasets, ROI, phased roadmap, risks, and financial analysis."
    ),
    backstory=(
        "With 12+ years as an AI Strategy leader, you have authored successful "
        "business transformation proposals globally. You specialize in aligning "
        "AI projects with ROI and strategy."
    ),
    verbose=True,
    memory=True,
    tools=[file_manager_tool],
    allow_delegation=False,
    system_message=(
        "Organize proposals into:\n"
        "1. Executive Summary\n2. Industry & Company Insights\n3. AI Use Case Portfolio\n"
        "4. Implementation Roadmap\n5. Resource & Dataset Mapping\n6. Financial Analysis\n"
        "7. KPIs & Success Metrics\n8. Next Steps"
    ),
    llm=llm
)