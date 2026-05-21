import psycopg2

connection = psycopg2.connect(
    host="localhost", database="devdb", user="hugo", password="123"
)

cursor = connection.cursor()

print("Conectado ao banco com sucesso!")

cursor.close()
connection.close()
