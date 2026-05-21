import psycopg2

connection = psycopg2.connect(
    host="localhost", database="devdb", user="hugo", password="123"
)

cursor = connection.cursor()

# UPDATE — updates the price of product with id=1
cursor.execute(
    """
    UPDATE products SET price = %s WHERE id = %s
""",
    (2999.00, 1),
)
connection.commit()
print("Product updated!")

# SELECT — checks if the update worked
cursor.execute("SELECT * FROM products")
products = cursor.fetchall()
for product in products:
    print(
        f"ID: {product[0]} | Name: {product[1]} | Price: ${product[2]} | Stock: {product[3]}"
    )

# DELETE — removes the product with id=1
cursor.execute("DELETE FROM products WHERE id = %s", (1,))
connection.commit()
print("\nProduct deleted!")

# SELECT — checks if the delete worked
cursor.execute("SELECT * FROM products")
products = cursor.fetchall()
print("Remaining products:")
for product in products:
    print(
        f"ID: {product[0]} | Name: {product[1]} | Price: ${product[2]} | Stock: {product[3]}"
    )

cursor.close()
connection.close()
