# routes/review/pickup_teacher.py

from flask import current_app
from routes.review import mysql

def get_teacher_ids(student_id):
    with current_app.app_context():
        try:
            cur = mysql.connection.cursor()
            cur.execute("SELECT teacher_id FROM matching_histories WHERE student_id = %s", (student_id,))
            teacher_ids = [row['teacher_id'] for row in cur.fetchall()]
            cur.close()
            print("Fetched teacher IDs:", teacher_ids)  # デバッグ用ログ出力
            return teacher_ids
        except Exception as e:
            print("Error fetching teacher IDs:", str(e))
            return []

def get_teacher_names(teacher_ids):
    with current_app.app_context():
        try:
            cur = mysql.connection.cursor()
            teacher_ids_tuple = tuple(teacher_ids) if len(teacher_ids) > 1 else (teacher_ids[0],)
            query = "SELECT id, name FROM teacher_profiles WHERE id IN %s" if len(teacher_ids) > 1 else "SELECT id, name FROM teacher_profiles WHERE id = %s"
            cur.execute(query, (teacher_ids_tuple,))
            teacher_names = {row['id']: row['name'] for row in cur.fetchall()}
            cur.close()
            print("Fetched teacher names:", teacher_names)  # デバッグ用ログ出力
            return teacher_names
        except Exception as e:
            print("Error fetching teacher names:", str(e))
            return {}
