import mysql.connector

# データベース接続の設定
db_config = {
    'user': 'team08',
    'password': 'pass08',
    'host': 'localhost',
    'database': 'MATCHINGAPP'
}

def insert_preference(student_id, subject, day, period):
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO student_preferences (student_id, subject, preferred_day, preferred_period)
            VALUES (%s, %s, %s, %s)
        """, (student_id, subject, day, period))

        conn.commit()
        
        # 挿入されたpreference_idを取得
        preference_id = cursor.lastrowid

        cursor.close()
        conn.close()

        return preference_id, "データベースに正常に挿入されました。"

    except mysql.connector.Error as err:
        return None, f"エラー: {err}"

