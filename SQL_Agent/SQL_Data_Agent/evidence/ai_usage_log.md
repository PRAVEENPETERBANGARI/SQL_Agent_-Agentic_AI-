**`evidence/ai_usage_log.md`**
This file fulfills the strict Human-in-the-Loop and Responsible AI requirements [cite: 21-27].

```markdown
# AI Usage Log & Human Review Notes

This log details the use of AI assistance during the development of the Retail SQL Data Analyst Agent, alongside the mandatory human review steps taken to ensure safety, correctness, and adherence to business logic.

| Date | AI Tool Used | Prompt/Task | Code/Output Generated | Human Validation Steps Taken |
|---|---|---|---|---|
| 2026-06-25 | Gemini | "Generate python script to load 5 CSVs into MySQL" | `database/load_data.py` | Reviewed the generated pandas code. Adjusted datetime formatting manually to ensure MySQL strict date compliance (YYYY-MM-DD). Verified missing data was handled correctly. |
| 2026-06-25 | Gemini | "Write a regular expression to block destructive SQL commands" | `src/safety.py` | Reviewed the `BLOCKED` keyword list. Tested the regex locally to ensure it correctly catches commands like DROP, DELETE, and UPDATE without producing false positives on safe SELECT queries. |
| 2026-06-26 | Gemini | "Help create a LangGraph state graph for this workflow" | `src/graph.py` | Audited the flow logic. Modified the LLM prompt to allow it to generate raw SQL (including unsafe ones) so that `safety.py` could intercept them appropriately. Verified state management structure. |
| 2026-06-26 | Gemini | "Generate 10 natural language test cases for retail data" | `outputs/test_case_results.csv` | Checked each test case against the provided SQL schema to ensure the questions made logical sense and that the expected SQL was valid. |

### Human-in-the-Loop Confirmation
* **Credentials:** Verified that no passwords, API keys, or confidential business data were pasted into AI prompts.
* **SQL Safety:** All AI-generated SQL execution is routed through `validate_sql` before hitting the database.
* **Accuracy:** I manually tested the generated agent to confirm the AI summaries correctly reflect the underlying synthetic dataset without hallucinating additional numbers.