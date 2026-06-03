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
def insert_product(name, price, stock):
    connection = psycopg2.connect(
        host="localhost", database="devdb", user="hugo", password="123"
    )
    cursor = connection.cursor()

    cursor.execute(
        """
        INSERT INTO products (name, price, stock)
        VALUES (%s, %s, %s)
    """,
        (name, price, stock),
    )
    connection.commit()
    print(f"Product '{name}' inserted successfully!")

    cursor.close()
    connection.close()


# Update price
def update_price(product_id, new_price):

    connection = psycopg2.connect(
        host="localhost", database="devdb", user="hugo", password="123"
    )
    cursor = connection.cursor()
    cursor.execute(
        """
    UPDATE products SET price = %s WHERE id = %s
""",
        (new_price, product_id),
    )
    connection.commit()
    print(f"Price updated successfully!")

    cursor.close()
    connection.close()


# DELETE — removes the product with id=1
def delete_product(product_id):
    connection = psycopg2.connect(
        host="localhost", database="devdb", user="hugo", password="123"
    )
    cursor = connection.cursor()

    cursor.execute("DELETE FROM products WHERE id = %s", (product_id,))
    connection.commit()
    print("\nProduct deleted!")
    cursor.close()
    connection.close()
