import psycopg2


# Search price
def search_by_price(min_price, max_price):

    connection = psycopg2.connect(
        host="localhost", database="devdb", user="hugo", password="123"
    )
    cursor = connection.cursor()
    cursor.execute(
        """
    SELECT * FROM products WHERE price BETWEEN %s AND %s
""",
        (min_price, max_price),
    )
    products = cursor.fetchall()
    for product in products:
        print(
            f"ID: {product[0]} | Name: {product[1]} | Price: ${product[2]} | Stock: {product[3]}"
        )

    connection.commit()
    cursor.close()
    connection.close()


# --- Testing ---
search_by_price(300, 500)
