from flask import current_app, g
from routes.profile.database_operations1 import get_db

# ログインIDからプロフィールIDを取得する関数
def get_profile_id(login_id):
    db = get_db()
    cursor = db.cursor()

    try:
        # ログインIDからemailとuser_typeを取得
        cursor.execute("SELECT email, user_type FROM login WHERE id = %s", (login_id,))
        result = cursor.fetchone()
        current_app.logger.debug(f"Login query result: {result}")

        if result is None:
            return None

        email, user_type = result

        # user_typeに基づいて適切なプロフィールIDを取得
        if user_type == 'student':
            cursor.execute("SELECT id FROM student_profiles WHERE email = %s", (email,))
            profile_result = cursor.fetchone()
        elif user_type == 'teacher':
            cursor.execute("SELECT id FROM teacher_profiles WHERE email = %s", (email,))
            profile_result = cursor.fetchone()
        else:
            return None

        current_app.logger.debug(f"Profile query result: {profile_result}")

        if profile_result is None:
            return None

        profile_id = profile_result[0]
        return profile_id

    finally:
        cursor.close()

