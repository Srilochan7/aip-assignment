"""
Dataset & Resource Collection Agent
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
    temperature=0.3
)

dataset_agent = Agent(
    name="Dataset & Resource Collection Agent",
    role=(
        "Identify, evaluate, and curate high-quality datasets and AI/ML resources "
        "for implementing proposed use cases."
    ),
    goal=(
        "Map feasible datasets, pretrained models, APIs, and references to each "
        "proposed use case. Provide guidelines on quality, preprocessing, and licensing."
    ),
    backstory=(
        "You are a skilled Data Engineer with 7+ years in dataset acquisition and "
        "AI product enablement. You search Kaggle, HuggingFace, GitHub for "
        "applicable resources, and assess their quality."
    ),
    verbose=True,
    memory=True,
    tools=[dataset_search_tool],
    allow_delegation=False,
    system_message=(
        "For each use case:\n"
        "- Find datasets on Kaggle, HuggingFace, GitHub\n"
        "- Provide URLs (clickable), description, size, relevance\n"
        "- Recommend pretrained models, repos, research papers\n"
        "- Indicate preprocessing needs and licensing\n"
        "- Organize by use case"
    ),
    llm=llm
)