from agents.planner_agent import planner_agent
from agents.sql_agent import sql_agent
from agents.response_agent import response_agent, normal_llm_response

def run_agent_pipeline(question: str):
    planner_result = planner_agent(question)

    if planner_result["tool_required"]:
        sql_result = sql_agent(question)
        response = response_agent(question, sql_result)
    else:
        response = normal_llm_response(question)

    return response

def main():
    test_questions = [
        # 1. Greeting / No Tool Required
        "Hello",
        "How are you today?",

        # 2. Business Metrics
        "How many customers do we have?",
        "How many payment failures occurred?",

        # 3. Customer Analytics
        "Which customers are from Texas?",
        "How many premium customers do we have?",

        # 4. Payment Analytics
        "Show all failed payments",
        "Which payment methods are used?",

        # 5. Restricted Access
        "Show all employee salaries",
        "What is Sarah's salary?",

        # 6. Read-Only Violation
        "Insert a new customer into customers table",
        "Delete all orders",

        # 7. Out of Schema
        "Give me yesterday weather near office",
        "Who won the NBA championship?",

        # 8. Ambiguous Business Questions
        "How is the business doing?",
        "Give me customer insights"

    ]

    for i, question in enumerate(test_questions, start=1):
        print("\n" + "=" * 80)
        print(f"QUESTION {i}: {question}")
        print("-" * 80)
        print("RESPONSE:", run_agent_pipeline(question))

if __name__ == "__main__":
    main()
