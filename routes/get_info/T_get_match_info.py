import mysql.connector
from flask import Flask, render_template

def get_db_connection():
    conn = mysql.connector.connect(
        host='localhost',
        user='team08',
        password='pass08',
        database='MATCHINGAPP'
    )
    return conn

def get_match_info(teacher_id):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    query = """
    SELECT mi.Match_datetime as date, 
           sp.name as name, 
           sp.gender as gender, 
           sp.preferred_gender as preferred_gender,
           sp.purpose as purpose,
           sp.target_school_level as target_school_level,
           sp.club_activity as club_activity,
           sp.school_type as school_type
    FROM MatchInfo mi
    JOIN student_profiles sp ON mi.Student_id = sp.id
    WHERE mi.Teacher_id = %s AND mi.Match_status = TRUE
    """
    cursor.execute(query, (teacher_id,))
    match_info = cursor.fetchall()

    cursor.close()
    conn.close()

    return match_info
