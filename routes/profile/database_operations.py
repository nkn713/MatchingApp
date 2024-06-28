# routes/profile/database_operations.py

from flask_mysqldb import MySQL
from flask import current_app
from routes.profile.error_handling import DatabaseError

mysql = MySQL()

def save_student_profile(email, name, gender, affiliation, grade):
    """Save student profile data to the database."""
    try:
        cur = mysql.connection.cursor()
        cur.execute(
            "INSERT INTO student_profiles (email, name, gender, affiliation, grade) VALUES (%s, %s, %s, %s, %s)",
            (email, name, gender, affiliation, grade)
        )
        mysql.connection.commit()
        cur.close()
    except Exception as e:
        current_app.logger.error(f"Failed to save student profile: {str(e)}")
        raise DatabaseError("Could not save student profile")

def save_teacher_profile(email, name, gender, affiliation, university):
    """Save teacher profile data to the database."""
    try:
        cur = mysql.connection.cursor()
        cur.execute(
            "INSERT INTO teacher_profiles (email, name, gender, affiliation, university) VALUES (%s, %s, %s, %s, %s)",
            (email, name, gender, affiliation, university)
        )
        mysql.connection.commit()
        cur.close()
    except Exception as e:
        current_app.logger.error(f"Failed to save teacher profile: {str(e)}")
        raise DatabaseError("Could not save teacher profile")
