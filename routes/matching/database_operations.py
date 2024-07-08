from flask_mysqldb import MySQL
from flask import current_app as app

mysql = MySQL()

def insert_or_update_teacher_profile(email, name, password, gender, exam_experience, deviation_value, club_activities, middle_school_type, teaching_style, introduction):
    cursor = mysql.connection.cursor()
    # teacher_profilesテーブルにデータを挿入または更新するSQL文を作成
    sql = """
    INSERT INTO teacher_profiles (email, name, password, gender, exam_experience, deviation_value, club_activities, middle_school_type, teaching_style, introduction)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
    ON DUPLICATE KEY UPDATE
        name = VALUES(name),
        password = VALUES(password),
        gender = VALUES(gender),
        exam_experience = VALUES(exam_experience),
        deviation_value = VALUES(deviation_value),
        club_activities = VALUES(club_activities),
        middle_school_type = VALUES(middle_school_type),
        teaching_style = VALUES(teaching_style);
        introduction = VALUES(introduction);
    """
    cursor.execute(sql, (email, name, password, gender, exam_experience, deviation_value, club_activities, middle_school_type, teaching_style))
    mysql.connection.commit()
    cursor.close()
