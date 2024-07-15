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
            print(f"Executing query: {query} with IDs: {teacher_ids}")

            # クエリの実行
            cursor.execute(query, tuple(teacher_ids))
            result = cursor.fetchall()
            print(f"Query result: {result}")

            # 結果をカラム名をキーとする辞書形式に変換
            teacher_profiles_list = []
            for teacher in result:
                teacher_dict = {
                    "id": teacher["id"],
                    "name": teacher["name"],
                    "email": teacher["email"],
                    "password": teacher["password"],
                    "gender": teacher["gender"],
                    "university": teacher["university"],
                    "department": teacher["department"],
                    "exam_experience": teacher["exam_experience"],
                    "deviation_value": teacher["deviation_value"],
                    "club_activities": teacher["club_activities"],
                    "middle_school_type": teacher["middle_school_type"],
                    "teaching_style": teacher["teaching_style"],
                    "introduction": teacher["introduction"]
                }
                teacher_profiles_list.append(teacher_dict)

            return teacher_profiles_list

    except Error as e:
        print("Error while connecting to MySQL", e)
        return None

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
