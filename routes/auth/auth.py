import mysql.connector
from mysql.connector import Error

def create_connection():
    """Create a database connection to the MySQL database."""
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='matchingapp',
            user='team08',
            password='pass08'
        )
        if connection.is_connected():
            return connection
    except Error as e:
        print(f"Error: '{e}'")
    return None

def authenticate_user(email, user_type):
    """Authenticate user by email and user_type."""
    connection = create_connection()
    if connection is None:
        return False

    try:
        cursor = connection.cursor(dictionary=True)
        query = "SELECT * FROM login WHERE email = %s AND user_type = %s"
        cursor.execute(query, (email, user_type))
        result = cursor.fetchone()
        cursor.close()
        connection.close()

        if result:
            return True
        else:
            return False
    except Error as e:
        print(f"Error: '{e}'")
        return False
