-- task_5.sql
INSERT INTO Customers (customer_id, customer_name, email, address)
VALUES (1, 'Cole Baidoo', 'cbaidoo@sandtech.com', '123 Happiness Ave.');
import mysql.connector

try:
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="1221SmTa",
        database="alx_book_store"
    )
    cursor = conn.cursor()
    cursor.execute("""
    INSERT INTO Customers (customer_id, customer_name, email, address)
    VALUES (1, 'Cole Baidoo', 'cbaidoo@sandtech.com', '123 Happiness Ave.');
    """)
    conn.commit()
    print("Customer inserted successfully!")
except mysql.connector.Error as err:
    print(f"Error: {err}")
finally:
    if conn.is_connected():
        cursor.close()
        conn.close()

