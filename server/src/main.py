import psycopg2
import config
try:
    connection = psycopg2.connect(
        dbname=config.DB_NAME,
        user=config.DB_USER,
        password=config.DB_PASS,
        host=config.DB_HOST,
        port=config.DB_PORT
    )
    
    cursor = connection.cursor()

    cursor.execute("SELECT version();")
    db_version = cursor.fetchone()

    print(f"Connected to the database. PostgreSQL version: {db_version}")

    cursor.close()
    connection.close()

except Exception as e:
    print(f"Error connecting to the database: {e}")