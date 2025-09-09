"""
Streamlit Web Application for AI Use Case Generation System
"""

import streamlit as st
import os
from config.crew import create_ai_usecase_crew
import time

# Page configuration
st.set_page_config(
    page_title="AI Use Case Generator",
    page_icon="🤖",
    layout="centered"
)

def main():
    """Main Streamlit application"""
    
    st.title("🤖 AI Use Case Generator")
    st.write("Enter a company name to generate AI use cases and implementation strategies.")
    
    # Simple form with just company name
    with st.form("generation_form"):
        company_name = st.text_input("Company Name", placeholder="e.g., Tesla")
        submit_button = st.form_submit_button("Analyze")

    # Process the request
    if submit_button:
        if not company_name.strip():
            st.error("Please enter a company name.")
        else:
            with st.spinner("Analyzing company and generating use cases..."):
                try:
                    crew_system = create_ai_usecase_crew(company_name.strip())
                    result = crew_system.kickoff()
                    
                    st.success("✅ Analysis completed!")
                    
                    # Show download buttons for results
                    company_slug = company_name.lower().replace(' ', '_')
                    output_dir = "outputs"
                    
                    st.subheader("📄 Download Reports")
                    
                    report_files = [
                        (f"{company_slug}_research_report.md", "Research Report"),
                        (f"{company_slug}_use_cases.md", "Use Cases"),
                        (f"{company_slug}_datasets_resources.md", "Datasets"),
                        (f"{company_slug}_final_proposal.md", "Final Proposal")
                    ]
                    
                    for filename, label in report_files:
                        filepath = os.path.join(output_dir, filename)
                        if os.path.exists(filepath):
                            with open(filepath, "r", encoding="utf-8") as f:
                                content = f.read()
                            st.download_button(
                                label=f"Download {label}",
                                data=content,
                                file_name=filename,
                                mime="text/markdown"
                            )
                
                except Exception as e:
                    st.error(f"Error: {str(e)}")

if __name__ == "__main__":
    main()