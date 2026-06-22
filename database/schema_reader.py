from database.queries import execute_select_query


ALLOWED_TABLES = ["employees", "customers", "orders", "payments"]


def get_database_schema() -> str:
    table_names = "', '".join(ALLOWED_TABLES)

    query = f"""
    SELECT table_name, column_name, data_type
    FROM information_schema.columns
    WHERE table_schema = 'public'
    AND table_name IN ('{table_names}')
    ORDER BY table_name, ordinal_position;
    """

    rows = execute_select_query(query)

    schema = {}

    for row in rows:
        table = row["table_name"]
        column = row["column_name"]
        data_type = row["data_type"]

        if table not in schema:
            schema[table] = []

        schema[table].append(f"- {column}: {data_type}")

    schema_text = ""

    for table, columns in schema.items():
        schema_text += f"Table: {table}\n"
        schema_text += "\n".join(columns)
        schema_text += "\n\n"

    return schema_text