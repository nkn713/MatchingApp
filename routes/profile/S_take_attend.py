import mysql.connector

# データベース接続の設定
db_config = {
    'user': 'team08',
    'password': 'pass08',
    'host': 'localhost',
    'database': 'MATCHINGAPP'
}

def insert_or_update_preference(student_id, subject, day, period):
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        cursor.execute("""
            SELECT * FROM student_preferences 
            WHERE student_id = %s AND subject = %s AND preferred_day = %s AND preferred_period = %s
        """, (student_id, subject, day, period))
        existing_record = cursor.fetchone()

        if existing_record:
            cursor.execute("""
                UPDATE student_preferences 
                SET subject = %s, preferred_day = %s, preferred_period = %s
                WHERE student_id = %s AND subject = %s AND preferred_day = %s AND preferred_period = %s
            """, (subject, day, period, student_id, subject, day, period))
        else:
            cursor.execute("""
                INSERT INTO student_preferences (student_id, subject, preferred_day, preferred_period)
                VALUES (%s, %s, %s, %s)
            """, (student_id, subject, day, period))

        conn.commit()
        cursor.close()
        conn.close()

        return "データベースに正常に挿入または更新されました。"

    except mysql.connector.Error as err:
        return f"エラー: {err}"
