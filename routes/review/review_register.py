# MatchingApp/routes/review/review_register.py

from flask import current_app
from routes.review import mysql

def register_review(student_id, teacher_id, rating, review):
    with current_app.app_context():
        try:
            cur = mysql.connection.cursor()
            query = """
                UPDATE match_histories
                SET rating = %s, review = %s
                WHERE student_id = %s AND teacher_id = %s
            """
            cur.execute(query, (rating, review, student_id, teacher_id))
            mysql.connection.commit()
            cur.close()
            return True
        except Exception as e:
            print("Error updating match_histories:", str(e))
            return False
