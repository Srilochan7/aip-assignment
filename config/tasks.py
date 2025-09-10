"""
Enhanced Task Configuration with Better Formatting Requirements
"""

import os
from crewai import Task

class TaskConfig:
    @staticmethod
    def _ensure_output_dir():
        os.makedirs("outputs", exist_ok=True)

    @staticmethod
    def create_research_task(research_agent, company_name: str):
        TaskConfig._ensure_output_dir()
        return Task(
            description=(
                f"Research {company_name} with professional formatting:\n\n"
                f"**Required Sections:**\n"
                f"1. 📊 Executive Summary (key findings, confidence levels)\n"
                f"2. 🏭 Industry Analysis (market size, CAGR, AI adoption %)\n"
                f"3. 🏢 Company Profile (revenue, employees, recent developments)\n"
                f"4. 🎯 Competitive Landscape (top 5 competitors, AI implementations)\n"
                f"5. 🔧 Technology Readiness (current stack, AI maturity score 1-10)\n"
                f"6. 📈 Strategic Opportunities (AI implementation potential)\n\n"
                f"**Formatting Requirements:**\n"
                f"- Use tables for quantitative data\n"
                f"- Include confidence indicators: 🟢 High | 🟡 Medium | 🔴 Low\n"
                f"- Add [📊 Source: Description](URL) for major claims\n"
                f"- Use > blockquotes for key insights\n"
                f"- Include **bold** for critical findings"
            ),
            expected_output=(
                f"Professional research report with:\n"
                f"- Executive summary with confidence matrix\n"
                f"- Structured industry analysis with metrics\n"
                f"- Comprehensive company assessment\n"
                f"- Competitive intelligence with AI benchmarks\n"
                f"- Technology readiness evaluation\n"
                f"- Strategic recommendations\n"
                f"- All sources properly cited with working links"
            ),
            agent=research_agent,
            output_file=f"outputs/{company_name.lower().replace(' ', '_')}_research.md",
        )

    @staticmethod
    def create_usecase_task(usecase_agent, company_name: str):
        TaskConfig._ensure_output_dir()
        return Task(
            description=(
                f"Generate structured AI use cases for {company_name}:\n\n"
                f"**Output Format:**\n"
                f"1. 📋 Executive Summary with priority matrix table\n"
                f"2. 🎯 Use Case Portfolio (10-12 detailed cases)\n"
                f"3. 📊 ROI & Complexity Analysis table\n"
                f"4. 🗺️ Implementation Timeline\n"
                f"5. 🏭 Industry Examples with verified links\n\n"
                f"**Use Case Structure:**\n"
                f"## 🚀 [Use Case Name]\n"
                f"- **Category:** 🟢 Quick Win | 🟡 Strategic | 🔴 Transformational\n"
                f"- **Problem:** Business challenge\n"
                f"- **Solution:** AI approach\n"
                f"- **Benefits:** Quantified value (%, $, time)\n"
                f"- **Timeline:** X months\n"
                f"- **ROI:** Expected return\n"
                f"- **Example:** [Company](URL) - success story\n\n"
                f"**Technology Coverage:**\n"
                f"Predictive Analytics, GenAI/LLMs, Computer Vision, Chatbots, Automation, Recommendations"
            ),
            expected_output=(
                f"Structured use case portfolio with:\n"
                f"- Professional executive summary\n"
                f"- 10-12 detailed use cases with business metrics\n"
                f"- Priority categorization matrix\n"
                f"- ROI analysis and complexity assessment\n"
                f"- Implementation timeline and roadmap\n"
                f"- Industry examples with working links\n"
                f"- Professional formatting with tables and emojis"
            ),
            agent=usecase_agent,
            output_file=f"outputs/{company_name.lower().replace(' ', '_')}_usecases.md",
        )

    @staticmethod
    def create_dataset_task(dataset_agent, company_name: str):
        TaskConfig._ensure_output_dir()
        return Task(
            description=(
                f"Curate verified datasets for {company_name} use cases:\n\n"
                f"**Search Requirements:**\n"
                f"- Kaggle: datasets and competitions with proper URLs\n"
                f"- HuggingFace: datasets and models with API validation\n"
                f"- GitHub: repositories with quality metrics\n\n"
                f"**Output Format:**\n"
                f"1. 📊 Executive Summary with quality overview table\n"
                f"2. Platform sections: 🏆 Kaggle | 🤗 HuggingFace | ⭐ GitHub\n"
                f"3. Quality assessment matrix\n"
                f"4. 💡 Implementation recommendations\n\n"
                f"**Resource Details:**\n"
                f"- Verified clickable links [Title](URL)\n"
                f"- Quality scores (1-10) with justification\n"
                f"- Use case mapping\n"
                f"- Access requirements and licensing\n"
                f"- Implementation priority recommendations"
            ),
            expected_output=(
                f"Comprehensive resource collection with:\n"
                f"- Executive summary with platform overview\n"
                f"- Verified datasets with quality assessments\n"
                f"- Pre-trained models and APIs\n"
                f"- Code repositories with star ratings\n"
                f"- Quality matrix and recommendations\n"
                f"- All links validated and properly formatted\n"
                f"- Implementation guidance and priorities"
            ),
            agent=dataset_agent,
            output_file=f"outputs/{company_name.lower().replace(' ', '_')}_resources.md",
        )

    @staticmethod
    def create_proposal_task(proposal_agent, company_name: str):
        TaskConfig._ensure_output_dir()
        return Task(
            description=(
                f"Create executive proposal for {company_name}:\n\n"
                f"**Document Structure:**\n"
                f"1. 🚀 Executive Summary (business impact, ROI, next steps)\n"
                f"2. 📊 Market Research & Industry Analysis\n"
                f"3. 🎯 AI Use Case Portfolio (prioritized with timelines)\n"
                f"4. 📚 Dataset & Resource Assets\n"
                f"5. 🗺️ Implementation Roadmap (phases, milestones)\n"
                f"6. 💰 Investment & ROI Analysis\n"
                f"7. ⚠️ Risk Management & Success Factors\n"
                f"8. 📞 Next Steps & Action Items\n"
                f"9. 📖 References & Sources\n\n"
                f"**Quality Requirements:**\n"
                f"- Professional executive tone\n"
                f"- Tables for comparisons and metrics\n"
                f"- Confidence indicators and priority matrices\n"
                f"- All links verified and clickable\n"
                f"- Cross-referenced findings from all agents\n"
                f"- Action-oriented recommendations"
            ),
            expected_output=(
                f"Executive-ready proposal with:\n"
                f"- Compelling executive summary\n"
                f"- Comprehensive market and company analysis\n"
                f"- Prioritized AI use case recommendations\n"
                f"- Verified resource and dataset catalog\n"
                f"- Detailed implementation roadmap\n"
                f"- Financial analysis and ROI projections\n"
                f"- Risk management framework\n"
                f"- Clear next steps and action plan\n"
                f"- Professional formatting with tables, matrices, and verified links"
            ),
            agent=proposal_agent,
            output_file=f"outputs/{company_name.lower().replace(' ', '_')}_proposal.md",
        )