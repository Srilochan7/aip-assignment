"""
File Management Tool for saving reports and datasets
"""

from crewai_tools import BaseTool
import os
from datetime import datetime
from typing import Dict, Any

class FileManagerTool(BaseTool):
    name: str = "File Manager Tool"
    description: str = "Save research reports, use cases, and dataset links to files"
    
    def __init__(self):
        super().__init__()
        self.output_dir = "outputs"
        self._ensure_output_directory()
    
    def _ensure_output_directory(self):
        """Ensure output directory exists"""
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)
    
    def _run(self, content: str, filename: str = None, file_type: str = "md") -> str:
        """Save content to file"""
        if not filename:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"report_{timestamp}"
        
        filepath = os.path.join(self.output_dir, f"{filename}.{file_type}")
        
        try:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            return f"Content saved successfully to {filepath}"
        except Exception as e:
            return f"Error saving file: {str(e)}"
    
    def save_research_report(self, content: str, company_name: str) -> str:
        """Save research report with structured naming"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{company_name.lower().replace(' ', '_')}_research_report_{timestamp}"
        return self._run(content, filename, "md")
    
    def save_use_cases(self, content: str, company_name: str) -> str:
        """Save use cases report"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{company_name.lower().replace(' ', '_')}_use_cases_{timestamp}"
        return self._run(content, filename, "md")
    
    def save_dataset_links(self, content: str, company_name: str) -> str:
        """Save dataset links"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{company_name.lower().replace(' ', '_')}_datasets_{timestamp}"
        return self._run(content, filename, "md")
    
    def save_final_proposal(self, content: str, company_name: str) -> str:
        """Save final proposal"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{company_name.lower().replace(' ', '_')}_final_proposal_{timestamp}"
        return self._run(content, filename, "md")

# Initialize the file manager tool
file_manager_tool = FileManagerTool()