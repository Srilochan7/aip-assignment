"""
Dataset Agent - Optimized
"""

from crewai import Agent, LLM
from tools.dataset_tool import dataset_search_tool
import os
from dotenv import load_dotenv

load_dotenv()
gemini_api_key = os.getenv("GEMINI_API_KEY")

llm = LLM(
    model="gemini/gemini-2.0-flash",
    api_key=gemini_api_key,
    temperature=0.25
)

dataset_agent = Agent(
    name="Dataset Curator",
    role="Data engineer specializing in dataset evaluation and curation",
    goal="Map quality datasets from Kaggle, HuggingFace, GitHub to each use case",
    backstory="7+ year data engineer with expertise in dataset quality assessment",
    verbose=True,
    memory=True,
    tools=[dataset_search_tool],
    allow_delegation=False,
    system_message=(
        "DATASET & RESOURCE CURATION:\n"
        "For each use case identify:\n"
        "1. PUBLIC DATASETS:\n"
        "   - [Dataset Name](URL) with quality score (1-10)\n"
        "   - Size, format, and use case mapping\n"
        "   - Data preparation requirements\n"
        "2. PRE-TRAINED MODELS:\n"
        "   - Model APIs and frameworks\n"
        "   - Performance benchmarks\n"
        "3. CODE REPOSITORIES:\n"
        "   - GitHub implementations with star ratings\n"
        "   - Documentation quality assessment\n"
        "4. COMMERCIAL APIS:\n"
        "   - Enterprise solutions and pricing\n"
        "Organize by use case priority tier with clickable links"
    ),
    llm=llm
)