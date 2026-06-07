import psycopg2


def delete_user(user_id):
    connection = psycopg2.connect(
        host="localhost", database="devdb", user="hugo", password="123"
    )
    cursor = connection.cursor()

    cursor.execute("DELETE FROM users WHERE id = %s", (user_id,))
    if cursor.rowcount == 0:
        print("User not found.")
    else:
        print("User deleted successfully!")
    connection.commit()
    cursor.close()
    connection.close()


delete_user(1)
