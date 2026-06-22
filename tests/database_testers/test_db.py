from database.queries import execute_select_query

query ="SELECT * from customers LIMIT 5"

response = execute_select_query(query)

print(response)