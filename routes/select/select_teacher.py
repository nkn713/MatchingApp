#講師選択処理部
import mysql.connector

def get_teacher_profile(teacher_id):
    # データベース接続の設定
    config = {
        'user': 'team08',
        'password': 'pass08',
        'host': 'localhost',
        'database': 'MATCHINGAPP'
    }

    try:
        # データベースに接続
        conn = mysql.connector.connect(**config)
        cursor = conn.cursor()

        # SQLクエリを実行
        query = "SELECT name, gender, affiliation, university FROM teacher_profiles WHERE id = %s"
        cursor.execute(query, (teacher_id,))

        # 結果を取得
        result = cursor.fetchone()

        # 接続を閉じる
        cursor.close()
        conn.close()

        if result:
            return list(result)
        else:
            return None

    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

''' 使用例
teacher_id = 1
profile = get_teacher_profile(teacher_id)
if profile:
    print(f"Teacher Profile: {profile}")
else:
    print("No profile found for the given ID.")
'''

import mysql.connector
from mysql.connector import Error
from datetime import datetime

def insert_match_info(student_email, teacher_email):
    try:
        # データベース接続の設定
        connection = mysql.connector.connect(
            host='localhost',
            database='MATCHINGAPP',
            user='team08',
            password='pass08'
        )

        if connection.is_connected():
            cursor = connection.cursor()

            # 挿入クエリの作成
            insert_query = """
            INSERT INTO MatchInfo (StudentEmail, TeacherEmail, MatchStatus, MatchDateTime)
            VALUES (%s, %s, %s, %s)
            """

            # クエリに渡すデータの準備
            match_status = True
            match_date_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            record = (student_email, teacher_email, match_status, match_date_time)

            # データの挿入
            cursor.execute(insert_query, record)
            connection.commit()
            print("Record inserted successfully into MatchInfo table")

    except Error as e:
        print(f"Error while connecting to MySQL: {e}")

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

'''使用例
insert_match_info("student@example.com", "teacher@example.com")
'''