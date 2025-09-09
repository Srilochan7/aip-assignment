"""
Crew Configuration for AI Use Case Generation System
"""

from crewai import Crew, Process
from agents.research_agent import research_agent
from agents.usecase_agent import usecase_agent
from agents.dataset_agent import dataset_agent
from agents.proposal_agent import proposal_agent
from config.tasks import TaskConfig


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
            output_log_file=f"outputs/{self.company_name.lower().replace(' ', '_')}_execution_log.txt"
        )
    
    def kickoff(self):
        """Execute the complete AI use case generation workflow"""
        crew = self.create_crew()
        result = crew.kickoff()
        return result


def create_ai_usecase_crew(company_name: str) -> AIUseCaseGenerationCrew:
    """Factory function to create AI use case generation crew"""
    return AIUseCaseGenerationCrew(company_name)