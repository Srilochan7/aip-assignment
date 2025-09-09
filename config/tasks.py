"""
Task Configuration for CrewAI workflow
"""

import os
from crewai import Task

class TaskConfig:
    @staticmethod
    def _ensure_output():
        os.makedirs("outputs", exist_ok=True)

    @staticmethod
    def create_research_task(agent, company):
        TaskConfig._ensure_output()
        return Task(
            description=f"Research {company} industry, strategy, competition.",
            expected_output="Research report in markdown with references.",
            agent=agent,
            output_file=f"outputs/{company.lower().replace(' ','_')}_research.md"
        )

    @staticmethod
    def create_usecase_task(agent, company):
        TaskConfig._ensure_output()
        return Task(
            description=f"Generate tailored AI/GenAI use cases for {company}.",
            expected_output="Portfolio of 10-15 AI/GenAI use cases.",
            agent=agent,
            output_file=f"outputs/{company.lower().replace(' ','_')}_usecases.md"
        )

    @staticmethod
    def create_dataset_task(agent, company):
        TaskConfig._ensure_output()
        return Task(
            description=f"Find datasets/resources for {company} AI use cases.",
            expected_output="Datasets, pretrained models, links.",
            agent=agent,
            output_file=f"outputs/{company.lower().replace(' ','_')}_datasets.md"
        )

    @staticmethod
    def create_proposal_task(agent, company):
        TaskConfig._ensure_output()
        return Task(
            description=f"Create executive-level AI proposal for {company}.",
            expected_output="Final markdown proposal.",
            agent=agent,
            output_file=f"outputs/{company.lower().replace(' ','_')}_proposal.md"
        )