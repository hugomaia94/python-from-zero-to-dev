import psycopg2

def update_email (user_id, new_email):
    connection = psycopg2.connect(
        host="localhost", database="devdb", user="hugo", password="123"
    )
    cursor = connection.cursor()
    cursor.execute(
        """
    UPDATE users SET email = %s WHERE id = %s
""",
        (new_email, user_id),
    )
    connection.commit()
    print(f"Email updated successfully!")

    cursor.close()
    connection.close()

update_email(2, "novoemail@teste.com")