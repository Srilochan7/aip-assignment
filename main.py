"""
Streamlit Web Application for AI Use Case Generation System
"""

import streamlit as st
from config.crew import create_ai_usecase_crew

# Page configuration
st.set_page_config(
    page_title="AI Use Case Generator",
    page_icon="🤖",
    layout="centered",
)

@st.cache_data
def run_crew_analysis(company_name: str) -> str:
    """Runs the CrewAI pipeline and returns ONLY the final proposal text (no file saving)."""
    crew_system = create_ai_usecase_crew(company_name)
    
    # Kickoff the workflow
    result = crew_system.kickoff()
    
    # Get ONLY the final proposal (last task output instead of writing files)
    final_proposal = result.output if hasattr(result, "output") else str(result)
    return final_proposal

def main():
    """Main Streamlit application"""
    
    st.title("🤖 AI Use Case Generator")
    st.write("Enter a company name to generate AI use cases and strategies.")
    
    company_name = st.text_input("Company Name", placeholder="e.g., Tesla")

    if st.button("Analyze Company"):
        if not company_name.strip():
            st.error("⚠️ Please enter a company name.")
        else:
            with st.spinner("🔍 Analyzing company and generating AI use cases..."):
                try:
                    # Run analysis (no file saving in outputs/)
                    final_result = run_crew_analysis(company_name.strip())
                    
                    st.success("✅ Analysis completed!")
                    
                    # Show the full report in the app
                    st.subheader("📑 Final Proposal")
                    st.markdown(final_result)
                    
                    # Allow download of report
                    st.download_button(
                        label="💾 Download Full Report",
                        data=final_result,
                        file_name=f"{company_name.lower().replace(' ', '_')}_final_proposal.md",
                        mime="text/markdown",
                    )
                except Exception as e:
                    st.error(f"❌ Error occurred: {str(e)}")

if __name__ == "__main__":
    main()