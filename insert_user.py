import psycopg2


def insert_user(name, email):

    connection = psycopg2.connect(
        host="localhost", database="devdb", user="hugo", password="123"
    )

    cursor = connection.cursor()
    # Inserts a user
    cursor.execute(
        """INSERT INTO users(name, email)
                   VALUES(%s,%s)""",
        (name, email),
    )

    # Without commit, nothing is actually saved
    connection.commit()

    print("User inserted successfully!")
    cursor.close()
    connection.close()


insert_user("Hugo Maia", "hugo@teste.com")
