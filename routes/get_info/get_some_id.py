import mysql.connector

# ログインIDからプロフィールIDを取得する関数
def get_profile_id(login_id):
    # MySQLデータベースに接続
    conn = mysql.connector.connect(
        host='localhost',
        user='team08',
        password='pass08',
        database='MATCHINGAPP'
    )
    cursor = conn.cursor()

    try:
        # ログインIDからemailとuser_typeを取得
        cursor.execute("SELECT email, user_type FROM login WHERE id = %s", (login_id,))
        result = cursor.fetchone()
        print(f"Login query result: {result}")

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

        print(f"Profile query result: {profile_result}")

        if profile_result is None:
            return None

        profile_id = profile_result[0]
        return profile_id

    finally:
        cursor.close()
        conn.close()
