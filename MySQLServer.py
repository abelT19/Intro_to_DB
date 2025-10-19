import mysql.connector

def create_database():
    try:
        # Connect to MySQL server (change user/password as needed)
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="yourpassword"
        )

        if connection.is_connected():
            cursor = connection.cursor()
            # Create database if not exists
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store;")
            print("Database 'alx_book_store' created successfully!")

    except mysql.connector.Error as err:
        print(f"Error while connecting to MySQL: {err}")

    finally:
        # Safely close the connection and cursor
        try:
            if connection.is_connected():
                cursor.close()
                connection.close()
        except NameError:
            pass  # connection was never established

if __name__ == "__main__":
    create_database()
