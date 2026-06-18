import psycopg2


# Search price
def search_by_name(name):

    connection = psycopg2.connect(
        host="localhost", database="devdb", user="hugo", password="123"
    )
    cursor = connection.cursor()
    cursor.execute(
        """
    SELECT * FROM users WHERE name ILIKE %s
""",
        (f"%{name}%",),
    )
    users = cursor.fetchall()
    for user in users:
        print(f"ID: {user[0]} | Name: {user[1]} | Email: {user[2]}")

    cursor.close()
    connection.close()


# --- Testing ---
search_by_name("hugo")
