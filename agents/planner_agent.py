import json
from llm.llm_client import call_llm


def build_planner_prompt(user_question: str) -> str:
    return f"""
You are a Planner Agent for an AI Business Intelligence system.

Your ONLY job is to decide whether the user's question should be routed to the SQL Agent.

Available Tool:
1. sql
- The SQL Agent can query the company database.
- The SQL Agent also handles:
  - unavailable schema questions
  - restricted access questions
  - read-only violation requests
  - database modification requests

Routing Rule:
- If the question is about company data, business data, customers, orders, payments, employees, salaries, revenue, metrics, reports, analytics, trends, counts, totals, regions, payment failures, customer insights, or business performance, route to SQL.
- If the question asks to insert, update, delete, drop, create, or modify database records, route to SQL.
- If the question asks for restricted data such as employee salaries, route to SQL.
- If the question asks for external factual information such as weather, sports, stock prices, or news, route to SQL so the SQL Agent can return that it is not answerable from the available schema.
- When uncertain, route to SQL.

Only return no tool for:
- greetings
- small talk
- casual conversation
- jokes
- general assistant conversation that clearly does not need company/database validation

Return ONLY valid JSON.
Do not include markdown.
Do not include explanations outside JSON.

If SQL is required:
{{
  "tool_required": true,
  "tools": ["sql"],
  "reason": "short reason"
}}

If no tool is required:
{{
  "tool_required": false,
  "tools": [],
  "reason": "short reason"
}}

User Question:
{user_question}
"""


def parse_planner_response(response_text: str) -> dict:
    try:
        return json.loads(response_text)
    except json.JSONDecodeError:
        return {
            "tool_required": False,
            "tools": [],
            "reason": "Planner returned invalid JSON."
        }


def planner_agent(user_question: str) -> dict:
    prompt = build_planner_prompt(user_question)
    response = call_llm(prompt)
    return parse_planner_response(response)