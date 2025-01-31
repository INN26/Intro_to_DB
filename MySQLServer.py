import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        # Connect to MySQL Server (Change credentials as needed)
        connection = mysql.connector.connect(
            host="localhost",     # Change if your MySQL server is not on localhost
            user="root", # Replace with your MySQL username
            password="Ndingiririkana0." # Replace with your MySQL password
        )

        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store;")
            print("Database 'alx_book_store' created successfully!")

    except mysql.connector.Error as e:
        print(f"Error: {e}")
   
    finally:
        # Close the connection
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection closed.")

if __name__ == "__main__":
    create_database()