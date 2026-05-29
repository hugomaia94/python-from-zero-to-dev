import psycopg2


def get_all_products():
    connection = psycopg2.connect(
        host="localhost", database="devdb", user="hugo", password="123"
    )
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM products")
    products = cursor.fetchall()
    for product in products:
        print(
            f"ID: {product[0]} | Name: {product[1]} | Price: ${product[2]} | Stock: {product[3]}"
        )
    cursor.close()
    connection.close()


get_all_products()
