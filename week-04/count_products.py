import psycopg2


# Search price
def count_products():

    connection = psycopg2.connect(
        host="localhost", database="devdb", user="hugo", password="123"
    )
    cursor = connection.cursor()
    cursor.execute(
        """
    SELECT COUNT(*) FROM products 
""",
      
    )
    
    total = cursor.fetchone()
    print(f"Total products: {total[0]}")

    cursor.close()
    connection.close()


count_products()