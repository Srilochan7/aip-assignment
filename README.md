# Research Agent 🤖

## 🗂️ Description

The Research Agent is a Streamlit-based web application designed to automate industry and company research, generating AI use cases and curated datasets. This project leverages the CrewAI framework, LangChain, and other cutting-edge libraries to provide a robust and user-friendly interface for research and analysis.

The Research Agent is ideal for researchers, analysts, and businesses seeking to streamline their research processes and gain valuable insights. With its intuitive UI and powerful backend, this application enables users to input a company name, generate AI use cases, and explore related datasets.

## ✨ Key Features

### Research Capabilities

* Conduct industry and company research using the Tavily Search Tool
* Generate AI use cases based on research findings
* Curate datasets for specific use cases

### Agent-based Architecture

* Research Agent: conducts industry and company research
* Use Case Agent: generates AI use cases
* Dataset Agent: curates datasets for specific use cases
* Proposal Agent: synthesizes findings into a structured markdown report

### Tech Integration

* CrewAI framework for agent-based architecture
* LangChain for language model interactions
* Streamlit for web application UI
* Tavily Search Tool for research capabilities

## 🗂️ Folder Structure

```mermaid
graph TD;
    src-->agents;
    src-->config;
    src-->tools;
    agents-->dataset_agent.py;
    agents-->research_agent.py;
    agents-->usecase_agent.py;
    agents-->proposal_agent.py;
    config-->crew.py;
    config-->tasks.py;
    tools-->tavily_tool.py;
    tools-->filemanager_tool.py;
    tools-->dataset_tool.py;
```

## 🛠️ Tech Stack

![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white&style=for-the-badge)
![Streamlit](https://img.shields.io/badge/Streamlit-1DA7FF?logo=streamlit&logoColor=white&style=for-the-badge)
![CrewAI](https://img.shields.io/badge/CrewAI-000?logo=crewai&logoColor=white&style=for-the-badge)
![LangChain](https://img.shields.io/badge/LangChain-000?logo=langchain&logoColor=white&style=for-the-badge)
![Tavily Search Tool](https://img.shields.io/badge/Tavily-000?logo=tavily&logoColor=white&style=for-the-badge)

## ⚙️ Setup Instructions

To run the Research Agent locally, follow these steps:

* Clone the repository: `git clone https://github.com/Srilochan7/research-agent.git`
* Install dependencies: `pip install -r requirements.txt`
* Set environment variables:
	+ Create a `.env` file in the root directory
	+ Add `TAVILY_API_KEY=your_api_key` to the `.env` file
* Run the application: `python run.py`

## 🤖 GitHub Actions

This repository uses GitHub Actions to automate testing and deployment. The workflow is defined in `.github/workflows/main.yml` and includes jobs for:

* Testing: runs unit tests and integration tests
* Deployment: deploys the application to a production environment

```mermaid
graph TD;
    workflow-->test;
    workflow-->deploy;
    test-->pytest;
    deploy-->streamlit;
```



<br><br>
<div align="center">
<img src="https://avatars.githubusercontent.com/u/142315222?v=4" width="120" />
<h3>lochan</h3>
<p>Building whatever.</p>
</div>
<br>
<p align="right">
<img src="https://gitfull.vercel.app/appLogo.png" width="20"/>  <a href="https://gitfull.vercel.app">Made by GitFull</a>
</p>
    