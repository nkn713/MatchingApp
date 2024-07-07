import mysql.connector
from mysql.connector import Error

def get_teacher_profiles(teacher_ids):
    try:
        # データベース接続の設定
        connection = mysql.connector.connect(
            host='localhost',
            database='MATCHINGAPP',
            user='team08',
            password='pass08'
        )

        if connection.is_connected():
            cursor = connection.cursor(dictionary=True)  # 結果を辞書形式で取得

            # SQLクエリの作成
            format_strings = ','.join(['%s'] * len(teacher_ids))
            query = f"SELECT * FROM teacher_profiles WHERE id IN ({format_strings})"

            # クエリの実行
            cursor.execute(query, tuple(teacher_ids))
            result = cursor.fetchall()

            return result

    except Error as e:
        print("Error while connecting to MySQL", e)
        return None

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

# 教師IDのリスト
#teacher_ids = [1, 2, 3]

# 教師プロフィールの取得
#profiles = get_teacher_profiles(teacher_ids)

# 教師の名前を取得して表示
#teacher_names = [profile['name'] for profile in profiles]
#print(teacher_names)
