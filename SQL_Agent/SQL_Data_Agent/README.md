# Retail SQL Data Analyst Agent
Automated setup complete. Please refer to the environment variables in `.env` and load your data into the `/data` folder.

## Overview
This project is an agentic AI solution that acts as a Retail SQL Data Analyst. It accepts natural language questions, translates them into MySQL queries using a LangGraph workflow, safely executes them against a local database, and summarizes the results. 

## Requirements
* Python 3.9+
* MySQL Workbench
* Windows PowerShell

## Setup Instructions

### 1. Database Configuration
1. Open MySQL Workbench.
2. Execute the `database/mysql_schema.sql` script to create the database and tables.
3. Ensure the synthetic CSV data files are placed in the `data/` directory.

### 2. Environment Variables
1. Rename `.env.example` to `.env`.
2. Update the `.env` file with your local MySQL credentials and Tiger AI Gateway/LLM details. **Do not commit the `.env` file to version control.**

### 3. Python Virtual Environment (Windows PowerShell)
Run the following commands in your terminal:
```powershell
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt

### 4. Load Data
Populate the MySQL tables with the CSV data:
python -m database.load_data

### 5. Running the Agent
Start the interactive CLI application:

python -m src.app

Type a natural language business question to interact with the database. Type exit to quit.


### Testing
Run the automated pytest suite to verify safety, memory, and SQL execution behavior:

PowerShell
pytest tests/