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
        query = "SELECT name, email FROM teacher_profiles WHERE id = %s"
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

from mysql.connector import Error
from datetime import datetime



def insert_match_status(student_email, teacher_email):
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

            # 挿入されたレコードのIDを取得
            match_id = cursor.lastrowid
            print("Record inserted successfully into MatchInfo table with MatchID:", match_id)
            return match_id

    except Error as e:
        print("Error while connecting to MySQL", e)
        return None

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

''' 使用例
student_email = "student@example.com"
teacher_email = "teacher@example.com"
match_id = insert_match_status(student_email, teacher_email)
if match_id:
    print(f"挿入されたマッチID: {match_id}")
else:
    print("挿入に失敗しました")
'''

'''使用例
insert_match_info("student@example.com", "teacher@example.com")
'''
