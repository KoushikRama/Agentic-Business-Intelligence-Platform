from llm.llm_client import call_llm


def build_response_prompt(question: str, sql_result: dict):
    return f"""
    You are a business intelligence assistant.

    Your job is to answer the user's question using the database result provided.

    Rules:
    - Be concise and business-friendly.
    - Do not mention internal implementation details unless useful.
    - If the database result contains a message, explain that message directly.
    - Do not invent data beyond the provided result.
    - If the result is empty, say no matching records were found.

    User Question:
    {question}

    SQL Query Used:
    {sql_result.get("sql_query")}

    Database Result:
    {sql_result.get("results")}

    Error:
    {sql_result.get("error")}

    Generate the final response:
    """


def response_agent(question: str, sql_result: dict):
    prompt = build_response_prompt(question, sql_result)
    return call_llm(prompt)


def normal_llm_response(question: str):
    prompt = f"""
    You are a helpful AI assistant for a business intelligence platform.

    The user's message does not require database access.

    Respond naturally and concisely.

    User Message:
    {question}
    """
    return call_llm(prompt)