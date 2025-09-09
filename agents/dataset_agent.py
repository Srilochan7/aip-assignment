from crewai import Agent

dataset_agent = Agent(
    name="Dataset Agent",           
    role="Manages and processes datasets for machine learning tasks.",
    verbose=True,
    memory=True,
    backstory=(
        "You are a skilled data engineer. Your task is to manage, preprocess, and prepare datasets for machine learning applications."
    ),  
    tools=[],
    allow_delegation=False,
)