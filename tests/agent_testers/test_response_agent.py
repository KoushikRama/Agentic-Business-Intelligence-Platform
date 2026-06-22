from agents.response_agent import normal_llm_response, response_agent

resp1= normal_llm_response("Hi,how are you?")
print("resp1:", resp1)
question2 = "Give me an SQL query to insert a customer into customers table"
results2 = [{'message': 'This request is not allowed because the system only supports read-only database access.'}]
resp2= response_agent(question2, results2)
print("resp2:",resp2)