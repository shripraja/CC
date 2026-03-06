import psycopg2

DB_HOST = "ep-royal-sound-a5vze9rq-pooler.us-east-2.aws.neon.tech"
DB_NAME = "neondb"
DB_USER = "neondb_owner"
DB_PASS = "npg_Ztv1oYdsI3Sq"

connection = None

try:
    connection = psycopg2.connect(
        host=DB_HOST,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASS
    )

    cursor = connection.cursor()
    cursor.execute("SELECT message FROM greetings WHERE id = 1;")
    result = cursor.fetchone()

    if result:
        print("Fetched from Neon DB:", result[0])
    else:
        print("No data found.")

except Exception as e:
    print("Error connecting to the database:", e)

finally:
    if connection:
        cursor.close()
        connection.close()
