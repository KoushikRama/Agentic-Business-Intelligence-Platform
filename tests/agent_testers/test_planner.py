from agents.planner_agent import planner_agent

questions = [
    "Hello, how are you?",
    "How many payment failures occurred?",
    "Which customers are from Texas?",
    "What is the total revenue?",
    "Tell me a joke."
]

for question in questions:
    print("\nQUESTION:", question)
    result = planner_agent(question)
    print("PLANNER RESULT:", result)