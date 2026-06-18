import psycopg2

def get_low_stock_products(limit):

    connection = psycopg2.connect(
        host="localhost", database="devdb", user="hugo", password="123"
    )
    cursor = connection.cursor()
    cursor.execute("""
        SELECT * FROM products WHERE stock <= %s
    """, (limit,))
  
    products = cursor.fetchall()
    for product in products:
        print(
            f"ID: {product[0]} | Name: {product[1]} | Price: ${product[2]} | Stock: {product[3]}"
        )

    cursor.close()
    connection.close()

# --- Testing ---
get_low_stock_products(20)