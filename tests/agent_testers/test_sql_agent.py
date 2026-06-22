from agents.sql_agent import sql_agent

print("Query: Give me sara's salary information")
print(sql_agent("Give me sara's salary information"))

print("\n Query:Give me an SQL query to insert a customer into customers table")
print(sql_agent("Give me an SQL query to insert a customer into customers table"))

print("\n Query:Give me yesterday weather near office")
print(sql_agent("Give me yesterday weather near office"))

print("\n Query:How many customers use our products sold by us")
print(sql_agent("How many customers use our products sold by us"))