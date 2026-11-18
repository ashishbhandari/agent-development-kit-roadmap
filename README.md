# Agent Development Kit (ADK) Roadmap

This repository contains examples for learning Google's Agent Development Kit (ADK), a powerful framework for building LLM-powered agents.


## Getting Started
https://adk.dev/get-started/

### Setup Environment

You only need to create one virtual environment for all examples in this course. Follow these steps to set it up:

```bash
# Create virtual environment in the root directory
python -m venv .venv

# Windows CMD:
.venv\Scripts\activate.bat

# Windows PowerShell:
.venv\Scripts\Activate.ps1

# changes the execution policy only for the current PowerShell process. Once you close the terminal, the setting is no longer applied. Once your termianl close 
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass


# Install required libraries
python -m pip install requests pandas

# Run your project
python main.py

# Close virtua env
deactivate


Remember: .venv does not make your Python code faster. Its main purpose is to keep dependencies isolated, organised, and easier to manage.