import psycopg2

connection = psycopg2.connect(
    host="localhost", database="devdb", user="hugo", password="123"
)

cursor = connection.cursor()

# Creates the user table if it doesn't exist yet
cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id     SERIAL PRIMARY KEY,
        name   VARCHAR(200) NOT NULL,
        email  VARCHAR(200) NOT NULL
    )
""")

# Without commit, nothing is actually saved
connection.commit()

print("Table created!")

cursor.close()
connection.close()
