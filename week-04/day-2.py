import psycopg2

connection = psycopg2.connect(
    host="localhost", database="devdb", user="hugo", password="123"
)

cursor = connection.cursor()

# Creates the products table if it doesn't exist yet
cursor.execute("""
    CREATE TABLE IF NOT EXISTS products (
        id     SERIAL PRIMARY KEY,
        name   VARCHAR(200) NOT NULL,
        price  DECIMAL(10, 2) NOT NULL,
        stock  INTEGER NOT NULL
    )
""")

# Inserts a product
cursor.execute(
    """
    INSERT INTO products (name, price, stock)
    VALUES (%s, %s, %s)
""",
    ("Notebook", 3500.00, 10),
)

# Without commit, nothing is actually saved
connection.commit()

print("Table created and product inserted!")

cursor.close()
connection.close()
