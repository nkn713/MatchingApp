import mysql.connector

# データベース接続の設定
db_config = {
    'user': 'team08',
    'password': 'pass08',
    'host': 'localhost',
    'database': 'MATCHINGAPP'
}

def insert_or_update_availability(teacher_id, subjects, days, periods):
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        for day in days:
            # 同じteacher_idとpreferred_dayのレコードを削除
            cursor.execute("""
                DELETE FROM teacher_preferences 
                WHERE teacher_id = %s AND preferred_day = %s
            """, (teacher_id, day))

            for subject in subjects:
                for period in periods:
                    # 新しいレコードを挿入
                    cursor.execute("""
                        INSERT INTO teacher_preferences (teacher_id, subject, preferred_day, preferred_period)
                        VALUES (%s, %s, %s, %s)
                    """, (teacher_id, subject, day, period))

        conn.commit()
        cursor.close()
        conn.close()

        return "データベースに正常に挿入または更新されました。"

    except mysql.connector.Error as err:
        return f"エラー: {err}"
