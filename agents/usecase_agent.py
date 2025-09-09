from crewai import Agent


usecase_agent = Agent(
    name="Use Case Agent",
    role="Identifies and defines use cases for a given product or service.",
    verbose=True,
    memory=True,
    backstory=("You are a strategic use case analyst. Your task is to identify and define potential use cases for products or services."),
    tools=[],
    allow_delegation=False,
)