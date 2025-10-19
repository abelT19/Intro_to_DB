import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        # Connect to MySQL server (update user/password as needed)
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="1221SmTa"
        )

        if connection.is_connected():
            cursor = connection.cursor()
            # Create database if not exists
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store;")
            print("Database 'alx_book_store' created successfully!")

    except Error as e:
        print(f"Error while connecting to MySQL: {e}")

    finally:
        # Safely close connection
        if connection.is_connected():
            cursor.close()
            connection.close()
            # Optional confirmation message
            # print("MySQL connection closed.")

if __name__ == "__main__":
    create_database()
