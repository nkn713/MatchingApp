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

        for subject in subjects:
            for day in days:
                for period in periods:
                    cursor.execute("""
                        SELECT * FROM teacher_preferences 
                        WHERE teacher_id = %s AND subject = %s AND preferred_day = %s AND preferred_period = %s
                    """, (teacher_id, subject, day, period))
                    existing_record = cursor.fetchone()

                    if existing_record:
                        cursor.execute("""
                            UPDATE teacher_preferences 
                            SET subject = %s, preferred_day = %s, preferred_period = %s
                            WHERE teacher_id = %s AND subject = %s AND preferred_day = %s AND preferred_period = %s
                        """, (subject, day, period, teacher_id, subject, day, period))
                    else:
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
