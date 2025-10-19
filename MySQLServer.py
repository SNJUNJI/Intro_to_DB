import mysql.connector
# Remove: from mysql.connector import Error

def create_database():
    connection = None
    try:
        # Establish connection to MySQL server
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password=''  # Adjust password as needed
        )
        
        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")
            
    except mysql.connector.Error as e:  # Use full qualified name here
        print(f"Error connecting to MySQL server: {e}")
    
    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()

if __name__ == "__main__":
    create_database()