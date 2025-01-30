import mysql.connector
from mysql.connector import Error

# MySQL Server Configuration - Update with your credentials
HOST = "localhost"  # Change if needed
USER = "root"  # Replace with your MySQL username
PASSWORD = "Ndingiririkana0."  # Replace with your MySQL password

def create_database():
    try:
        # Connect to MySQL Server (without selecting a database)
        connection = mysql.connector.connect(host=HOST, user=USER, password=PASSWORD)
        cursor = connection.cursor()
        
        # Create the database if it doesn't exist
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        
        print("Database 'alx_book_store' created successfully!")

    except Error as e:
        print(f"Error connecting to MySQL: {e}")

    finally:
        # Close cursor and connection safely
        if cursor is not None:
            cursor.close()
        if connection is not None and connection.is_connected():
            connection.close()
            print("MySQL connection closed.")

# Run the function
if __name__ == "__main__":
    create_database()