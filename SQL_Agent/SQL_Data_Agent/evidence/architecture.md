project_root/
├── data/                      # Synthetic CSV datasets
│   ├── customers.csv
│   ├── products.csv
│   ├── returns.csv
│   ├── sales_transactions.csv
│   └── stores.csv
├── database/                  # Database initialization scripts
│   ├── load_data.py           # Pandas script to load CSVs into MySQL
│   ├── mysql_schema.sql       # DDL script to create tables
│   └── schema_reference.md    # Reference for LLM prompting
├── evidence/                  # Submission evidence
│   └── ai_usage_log.md        # Human-in-the-loop and AI prompt logs
├── outputs/                   # Test results and artifacts
│   └── test_case_results.csv  # 10 manual conversational test cases
├── src/                       # Core application code
│   ├── __init__.py
│   ├── app.py                 # Interactive CLI application
│   ├── config.py              # Environment variable loader
│   ├── graph.py               # LangGraph state and node definitions
│   ├── memory.py              # Conversation history management
│   ├── safety.py              # SQL validation and guardrails
│   ├── sql_tools.py           # MySQL execution tool
│   └── tiger_gateway_client.py# LLM API interface
├── tests/                     # Automated testing suite
│   ├── __init__.py
│   ├── test_memory.py         # Pytest: context retention
│   ├── test_safety.py         # Pytest: destructive SQL blocking
│   └── test_sql_tools.py      # Pytest: DB error handling
├── .env                       # Local secrets (Not committed)
├── .env.example               # Template for environment variables
├── README.md                  # Project documentation (this file)
└── requirements.txt           # Python dependencies