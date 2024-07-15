import mysql.connector
from mysql.connector import errorcode

# データベース接続の設定
db_config = {
    'user': 'team08',
    'password': 'pass08',
    'host': 'localhost',
    'database': 'MATCHINGAPP',
    'port':'50800'
}

def insert_or_update_availability(teacher_id, subjects, day, periods):
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        # 同じteacher_idとpreferred_dayのレコードを削除
        print(f"Deleting existing records for teacher_id={teacher_id}, day={day}")
        cursor.execute("""
            DELETE FROM teacher_preferences 
            WHERE teacher_id = %s AND preferred_day = %s
        """, (teacher_id, day))

        for subject in subjects:
            for period in periods:
                # 新しいレコードを挿入
                print(f"Inserting: teacher_id={teacher_id}, subject={subject}, day={day}, period={period}")
                cursor.execute("""
                    INSERT INTO teacher_preferences (teacher_id, subject, preferred_day, preferred_period)
                    VALUES (%s, %s, %s, %s)
                """, (teacher_id, subject, day, period))

        conn.commit()
        cursor.close()
        conn.close()

        print("データベースに正常に挿入または更新されました。")
        return "データベースに正常に挿入または更新されました。"

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
        return f"エラー: {err}"
