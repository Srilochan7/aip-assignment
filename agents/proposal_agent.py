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
    role="Senior AI Strategy Consultant creating structured executive-ready reports.",
    goal=(
        "Synthesize research findings, use cases, and resource mappings into ONE unified "
        "report, written in markdown with clear structure, clickable links, and references."
    ),
    backstory="12+ year AI Strategy Consultant who organizes proposals for C‑level execs.",
    verbose=True,
    memory=True,
    tools=[file_manager_tool],
    allow_delegation=False,
    system_message=(
        "Take the outputs from Research, Use Case, and Dataset agents.\n"
        "Combine them into one SINGLE markdown report with this structure:\n\n"
        "# Market Research & Use Case Generation Report\n\n"
        "## 1. Market Research & Industry Analysis\n"
        "- Insert research agent results\n\n"
        "## 2. AI / GenAI Use Case Proposals\n"
        "- Insert use case agent results\n\n"
        "## 3. Dataset & Resource Assets\n"
        "- Insert dataset agent results (ensure clickable links)\n\n"
        "## 4. Final Proposal & Recommendations\n"
        "- Insert key recommendations, roadmap, ROI\n\n"
        "## References\n"
        "- Add citations and sources\n\n"
        "👉 The entire report must read like a professional consulting document."
    ),
    llm=llm
)