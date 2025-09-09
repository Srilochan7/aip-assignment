"""
Streamlit Web Application for AI Use Case Generation System
"""

import streamlit as st
import os
from datetime import datetime
import plotly.graph_objects as go
import plotly.express as px
from config.crew import create_ai_usecase_crew
import threading
import time

# Page configuration
st.set_page_config(
    page_title="AI Use Case Generator",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        color: #1e88e5;
        text-align: center;
        margin-bottom: 2rem;
    }
    .sub-header {
        font-size: 1.5rem;
        color: #424242;
        margin-bottom: 1rem;
    }
    .info-box {
        background-color: #f5f5f5;
        padding: 1rem;
        border-radius: 10px;
        margin: 1rem 0;
    }
    .success-box {
        background-color: #e8f5e8;
        padding: 1rem;
        border-radius: 10px;
        border-left: 5px solid #4caf50;
    }
    .agent-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 1rem;
        border-radius: 10px;
        margin: 0.5rem 0;
    }
</style>
""", unsafe_allow_html=True)


def display_system_architecture():
    """Display the system architecture flowchart"""
    st.markdown('<h2 class="sub-header">🏗️ System Architecture</h2>', unsafe_allow_html=True)
    
    # Create a flowchart using Plotly
    fig = go.Figure()
    
    # Define nodes
    nodes = {
        'Input': {'x': 0.1, 'y': 0.5, 'color': '#ff6b6b'},
        'Research Agent': {'x': 0.3, 'y': 0.8, 'color': '#4ecdc4'},
        'Use Case Agent': {'x': 0.5, 'y': 0.8, 'color': '#45b7d1'},
        'Dataset Agent': {'x': 0.7, 'y': 0.8, 'color': '#96ceb4'},
        'Proposal Agent': {'x': 0.9, 'y': 0.5, 'color': '#feca57'},
        'Output': {'x': 0.9, 'y': 0.2, 'color': '#ff9ff3'}
    }
    
    # Add nodes
    for name, props in nodes.items():
        fig.add_trace(go.Scatter(
            x=[props['x']], 
            y=[props['y']],
            mode='markers+text',
            marker=dict(size=80, color=props['color']),
            text=name,
            textposition="middle center",
            textfont=dict(size=12, color='white'),
            showlegend=False
        ))
    
    # Add arrows (simplified representation)
    arrows = [
        ('Input', 'Research Agent'),
        ('Research Agent', 'Use Case Agent'),
        ('Use Case Agent', 'Dataset Agent'),
        ('Dataset Agent', 'Proposal Agent'),
        ('Proposal Agent', 'Output')
    ]
    
    for start, end in arrows:
        start_node = nodes[start]
        end_node = nodes[end]
        fig.add_annotation(
            x=end_node['x'], y=end_node['y'],
            ax=start_node['x'], ay=start_node['y'],
            xref='x', yref='y',
            axref='x', ayref='y',
            arrowhead=2,
            arrowsize=1,
            arrowwidth=2,
            arrowcolor='#34495e'
        )
    
    fig.update_layout(
        title="AI Use Case Generation System Architecture",
        xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
        yaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
        plot_bgcolor='rgba(0,0,0,0)',
        height=400
    )
    
    st.plotly_chart(fig, use_container_width=True)


def display_agent_info():
    """Display information about each agent"""
    st.markdown('<h2 class="sub-header">🤖 Multi-Agent System</h2>', unsafe_allow_html=True)
    
    agents_info = [
        {
            "name": "🔍 Research Agent",
            "role": "Industry & Company Analysis",
            "description": "Conducts comprehensive market research, analyzes industry trends, and evaluates company positioning."
        },
        {
            "name": "💡 Use Case Agent", 
            "role": "AI/GenAI Solution Design",
            "description": "Generates relevant AI/ML use cases based on industry analysis and company needs."
        },
        {
            "name": "📊 Dataset Agent",
            "role": "Resource Collection",
            "description": "Identifies and curates relevant datasets from Kaggle, HuggingFace, and GitHub."
        },
        {
            "name": "📋 Proposal Agent",
            "role": "Strategic Planning",
            "description": "Synthesizes findings into executive-ready implementation proposals."
        }
    ]
    
    cols = st.columns(2)
    for i, agent in enumerate(agents_info):
        with cols[i % 2]:
            st.markdown(f"""
            <div class="agent-card">
                <h3>{agent['name']}</h3>
                <p><strong>{agent['role']}</strong></p>
                <p>{agent['description']}</p>
            </div>
            """, unsafe_allow_html=True)


def main():
    """Main Streamlit application"""
    
    # Header
    st.markdown('<h1 class="main-header">🤖 AI Use Case Generator</h1>', unsafe_allow_html=True)
    st.markdown("**Professional Multi-Agent System for AI/GenAI Use Case Generation**")
    
    # Sidebar configuration
    with st.sidebar:
        st.markdown("## ⚙️ Configuration")
        
        # API Key validation
        st.markdown("### API Keys")
        openai_key = st.text_input("OpenAI API Key", type="password", help="Required for LLM operations")
        tavily_key = st.text_input("Tavily API Key", type="password", help="Required for web search")
        
        if openai_key:
            os.environ["OPENAI_API_KEY"] = openai_key
        if tavily_key:
            os.environ["TAVILY_API_KEY"] = tavily_key
        
        st.markdown("### Model Settings")
        model = st.selectbox("OpenAI Model", ["gpt-4-turbo-preview", "gpt-4", "gpt-3.5-turbo"], index=0)
        temperature = st.slider("Temperature", 0.0, 1.0, 0.7, 0.1)
        
        os.environ["OPENAI_MODEL"] = model
        os.environ["TEMPERATURE"] = str(temperature)
        
        st.markdown("---")
        st.markdown("### 📚 Resources")
        st.markdown("- [CrewAI Documentation](https://docs.crewai.com)")
        st.markdown("- [Tavily Search API](https://tavily.com)")
        st.markdown("- [Kaggle Datasets](https://kaggle.com/datasets)")
        st.markdown("- [HuggingFace Hub](https://huggingface.co)")
    
    # Main content tabs
    tab1, tab2, tab3, tab4 = st.tabs(["🏠 Home", "🚀 Generate", "📊 Results", "📖 Documentation"])
    
    with tab1:
        st.markdown('<div class="info-box">', unsafe_allow_html=True)
        st.markdown("""
        ### Welcome to the AI Use Case Generation System
        
        This professional multi-agent system helps organizations identify and prioritize AI/ML opportunities 
        by conducting comprehensive market research and generating tailored use cases.
        
        **Key Features:**
        - 🔍 **Comprehensive Research**: Industry analysis and competitive intelligence
        - 💡 **Custom Use Cases**: AI/GenAI solutions tailored to your business
        - 📊 **Dataset Curation**: Relevant resources from top platforms
        - 📋 **Executive Proposals**: Professional implementation roadmaps
        """)
        st.markdown('</div>', unsafe_allow_html=True)
        
        display_system_architecture()
        display_agent_info()
    
    with tab2:
        st.markdown('<h2 class="sub-header">🚀 Generate AI Use Cases</h2>', unsafe_allow_html=True)
        
        # Input form
        with st.form("generation_form"):
            company_name = st.text_input(
                "Company Name", 
                placeholder="e.g., Tesla, Amazon, Microsoft",
                help="Enter the company name for analysis"
            )
            
            industry_hint = st.selectbox(
                "Industry (Optional Hint)",
                ["Auto-detect", "Automotive", "Manufacturing", "Finance", "Retail", "Healthcare", 
                 "Technology", "Energy", "Telecommunications", "Real Estate", "Other"]
            )
            
            additional_context = st.text_area(
                "Additional Context (Optional)",
                placeholder="Any specific focus areas, challenges, or requirements...",
                help="Provide additional context to improve analysis quality"
            )
            
            submit_button = st.form_submit_button("🚀 Generate Use Cases", type="primary")
        
        # Validation and execution
        if submit_button:
            if not company_name:
                st.error("Please enter a company name.")
            elif not openai_key or not tavily_key:
                st.error("Please provide both OpenAI and Tavily API keys in the sidebar.")
            else:
                # Store session state
                st.session_state.company_name = company_name
                st.session_state.industry_hint = industry_hint
                st.session_state.additional_context = additional_context
                
                # Execute workflow
                with st.spinner("🤖 AI Agents are working on your request..."):
                    try:
                        # Progress tracking
                        progress_bar = st.progress(0)
                        status_text = st.empty()
                        
                        # Create and execute crew
                        crew_system = create_ai_usecase_crew(company_name)
                        
                        # Simulate progress updates
                        progress_steps = [
                            "🔍 Research Agent: Analyzing industry and company...",
                            "💡 Use Case Agent: Generating AI/ML use cases...",
                            "📊 Dataset Agent: Collecting relevant datasets...",
                            "📋 Proposal Agent: Creating final proposal..."
                        ]
                        
                        for i, step in enumerate(progress_steps):
                            status_text.text(step)
                            progress_bar.progress((i + 1) * 25)
                            time.sleep(1)  # Simulate work
                        
                        # Execute the crew (this would be the actual execution)
                        result = crew_system.kickoff()
                        
                        progress_bar.progress(100)
                        status_text.text("✅ Analysis complete!")
                        
                        st.session_state.analysis_complete = True
                        st.session_state.result = result
                        
                        st.success("🎉 AI use case analysis completed successfully!")
                        st.info("Check the 'Results' tab to view the generated reports.")
                        
                    except Exception as e:
                        st.error(f"An error occurred during analysis: {str(e)}")
                        st.error("Please check your API keys and try again.")
    
    with tab3:
        st.markdown('<h2 class="sub-header">📊 Analysis Results</h2>', unsafe_allow_html=True)
        
        if hasattr(st.session_state, 'analysis_complete') and st.session_state.analysis_complete:
            company_name = st.session_state.company_name
            
            # Display results summary
            st.markdown('<div class="success-box">', unsafe_allow_html=True)
            st.markdown(f"### ✅ Analysis completed for **{company_name}**")
            st.markdown(f"**Generated on:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
            st.markdown('</div>', unsafe_allow_html=True)
            
            # File downloads
            st.markdown("### 📁 Generated Reports")
            
            output_dir = "outputs"
            company_slug = company_name.lower().replace(' ', '_')
            
            report_files = [
                (f"{company_slug}_research_report.md", "🔍 Industry Research Report"),
                (f"{company_slug}_use_cases.md", "💡 AI Use Cases Portfolio"),
                (f"{company_slug}_datasets_resources.md", "📊 Dataset & Resources Collection"),
                (f"{company_slug}_final_proposal.md", "📋 Executive Proposal"),
                (f"{company_slug}_execution_log.txt", "📝 Execution Log")
            ]
            
            cols = st.columns(len(report_files))
            for i, (filename, description) in enumerate(report_files):
                with cols[i]:
                    filepath = os.path.join(output_dir, filename)
                    if os.path.exists(filepath):
                        with open(filepath, 'r', encoding='utf-8') as f:
                            content = f.read()
                        st.download_button(
                            label=description,
                            data=content,
                            file_name=filename,
                            mime='text/markdown' if filename.endswith('.md') else 'text/plain'
                        )
                    else:
                        st.warning(f"File not found: {filename}")
            
            # Display preview of final proposal
            proposal_path = os.path.join(output_dir, f"{company_slug}_final_proposal.md")
            if os.path.exists(proposal_path):
                st.markdown("### 📋 Final Proposal Preview")
                with open(proposal_path, 'r', encoding='utf-8') as f:
                    proposal_content = f.read()[:2000]  # Show first 2000 characters
                st.markdown(f"```markdown\n{proposal_content}...\n```")
                
        else:
            st.info("No analysis results available. Please run the analysis first in the 'Generate' tab.")
    
    with tab4:
        st.markdown('<h2 class="sub-header">📖 Documentation</h2>', unsafe_allow_html=True)
        
        