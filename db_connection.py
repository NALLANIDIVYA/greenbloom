import mysql.connector

def get_connection():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="divya123",
        database="green_bloom_db"
    )

    return conn