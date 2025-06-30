import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(
            host='127.0.0.1',
            user='root',
            password='Zamaleksc_2003',
            database='alx_book_store', )
    if connection.is_connected():
        db_info = connection.is_connected()
        if db_info:
            cursor = connection.cursor()
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully")
        
except mysql.connector.Error as err:
    print(f"Error while connecting to MySQL: {err}")

finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")



