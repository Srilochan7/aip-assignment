"""
Crew Configuration for AI Use Case Generation System
"""

from crewai import Crew, Process
from agents.research_agent import research_agent
from agents.usecase_agent import usecase_agent
from agents.dataset_agent import dataset_agent
from agents.proposal_agent import proposal_agent
from config.tasks import TaskConfig
import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

# Load environment variables
load_dotenv()

class AIUseCaseGenerationCrew:
    """Main crew orchestrator for AI use case generation workflow"""
    
    def __init__(self, company_name: str):
        self.company_name = company_name
        self.task_config = TaskConfig()
        
        # Initialize tasks
        self.research_task = self.task_config.create_research_task(
            research_agent, self.company_name
        )
        self.usecase_task = self.task_config.create_usecase_task(
            usecase_agent, self.company_name
        )
        self.dataset_task = self.task_config.create_dataset_task(
            dataset_agent, self.company_name
        )
        self.proposal_task = self.task_config.create_proposal_task(
            proposal_agent, self.company_name
        )
        
        # Set task dependencies
        self.usecase_task.context = [self.research_task]
        self.dataset_task.context = [self.research_task, self.usecase_task]
        self.proposal_task.context = [self.research_task, self.usecase_task, self.dataset_task]
    
    def create_crew(self) -> Crew:
        """Create and configure the crew with agents and tasks"""
        # Get Gemini API key
        gemini_api_key = os.getenv("GEMINI_API_KEY")
        
        # Create LLM instance for the crew
        crew_llm = ChatGoogleGenerativeAI(
            verbose=True,
            temperature=0.4,
            model="gemini-2.0-flash",
            api_key=gemini_api_key
        )
        
        return Crew(
            agents=[
                research_agent,
                usecase_agent,
                dataset_agent,
                proposal_agent
            ],
            tasks=[
                self.research_task,
                self.usecase_task,
                self.dataset_task,
                self.proposal_task
            ],
            process=Process.sequential,
            verbose=True,
            memory=True,
            planning=True,
            output_log_file=f"outputs/{self.company_name.lower().replace(' ', '_')}_execution_log.txt",
            llm=crew_llm  # This is the key fix - specify the LLM for the crew
        )
    
    def kickoff(self):
        """Execute the complete AI use case generation workflow"""
        crew = self.create_crew()
        result = crew.kickoff()
        return result


def create_ai_usecase_crew(company_name: str) -> AIUseCaseGenerationCrew:
    """Factory function to create AI use case generation crew"""
    return AIUseCaseGenerationCrew(company_name)