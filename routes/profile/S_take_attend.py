from flask import current_app
from routes.profile.database_operations1 import get_db

def insert_preference(student_id, subject, day, period):
    if student_id is None or subject is None or day is None or period is None:
        return None, "エラー: 入力された値のいずれかがNULLです。"

    try:
        db = get_db()
        cursor = db.cursor()

        cursor.execute("""
            INSERT INTO student_preferences (student_id, subject, preferred_day, preferred_period)
            VALUES (%s, %s, %s, %s)
        """, (student_id, subject, day, period))

        db.commit()

        # 挿入されたpreference_idを取得
        preference_id = cursor.lastrowid

        cursor.close()

        return preference_id, "データベースに正常に挿入されました。"

    except Exception as err:
        current_app.logger.error(f"エラー: {err}")
        return None, f"エラー: {err}"

def check_student_profile_complete(student_id):
    try:
        db = get_db()
        cursor = db.cursor()

        # student_profiles テーブルから指定された student_id のレコードを取得
        query = "SELECT * FROM student_profiles WHERE id = %s"
        cursor.execute(query, (student_id,))
        record = cursor.fetchone()

        # レコードが存在しない場合
        if record is None:
            return False

        # レコードの各フィールドをチェックしてnullがあるか確認
        for field in record:
            if field is None:
                return False

        cursor.close()

        return True

    except Exception as err:
        current_app.logger.error(f"エラー: {err}")
        return False
