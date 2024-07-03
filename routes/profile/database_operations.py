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

def update_student_profile(email, name=None, gender=None, affiliation=None, grade=None):
    """Update student profile data in the database."""
    try:
        cur = mysql.connection.cursor()
        fields = []
        values = []
        if name is not None:
            fields.append("name = %s")
            values.append(name)
        if gender is not None:
            fields.append("gender = %s")
            values.append(gender)
        if affiliation is not None:
            fields.append("affiliation = %s")
            values.append(affiliation)
        if grade is not None:
            fields.append("grade = %s")
            values.append(grade)
        
        values.append(email)
        cur.execute(
            f"UPDATE student_profiles SET {', '.join(fields)} WHERE email = %s",
            values
        )
        mysql.connection.commit()
        cur.close()
    except Exception as e:
        current_app.logger.error(f"Failed to update student profile: {str(e)}")
        raise DatabaseError("Could not update student profile")

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

def update_teacher_profile(email, name=None, gender=None, affiliation=None, university=None):
    """Update teacher profile data in the database."""
    try:
        cur = mysql.connection.cursor()
        fields = []
        values = []
        if name is not None:
            fields.append("name = %s")
            values.append(name)
        if gender is not None:
            fields.append("gender = %s")
            values.append(gender)
        if affiliation is not None:
            fields.append("affiliation = %s")
            values.append(affiliation)
        if university is not None:
            fields.append("university = %s")
            values.append(university)
        
        values.append(email)
        cur.execute(
            f"UPDATE teacher_profiles SET {', '.join(fields)} WHERE email = %s",
            values
        )
        mysql.connection.commit()
        cur.close()
    except Exception as e:
        current_app.logger.error(f"Failed to update teacher profile: {str(e)}")
        raise DatabaseError("Could not update teacher profile")
    