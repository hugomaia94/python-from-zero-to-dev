import psycopg2


def get_all_users():
    connection = psycopg2.connect(
        host="localhost", database="devdb", user="hugo", password="123"
    )
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    for user in users:
        print(f"ID: {user[0]} | Name: {user[1]} | email: {user[2]}")
    cursor.close()
    connection.close()


get_all_users()
