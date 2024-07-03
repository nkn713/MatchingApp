import mysql.connector
from mysql.connector import Error

def insert_match_history(student_id, teacher_id):
    try:
        # データベース接続の設定
        connection = mysql.connector.connect(
            host='localhost',  # 適切なホスト名を設定
            database='MATCHINGAPP',  # 適切なデータベース名を設定
            user='team08',  # 適切なユーザー名を設定
            password='pass08'  # 適切なパスワードを設定
        )

        if connection.is_connected():
            cursor = connection.cursor()

            # SQLクエリの定義
            insert_query = """
            INSERT INTO match_histories (student_id, teacher_id)
            VALUES (%s, %s)
            """

            # データをタプルにして準備
            data_tuple = (student_id, teacher_id)

            # SQLクエリを実行
            cursor.execute(insert_query, data_tuple)
            connection.commit()

            print(f"Match history inserted successfully: {cursor.rowcount} row(s) affected")
            return True

    except Error as e:
        print(f"Error while connecting to MySQL: {e}")
        return False

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

# 関数の使用例
'''
result = insert_match_history(1, 2)
print("Success" if result else "Failed")
'''


def update_match_history(history_id, rating, review):
    try:
        # データベース接続の設定
        connection = mysql.connector.connect(
            host='localhost',  # 適切なホスト名を設定
            database='MATCHINGAPP',  # 適切なデータベース名を設定
            user='team08',  # 適切なユーザー名を設定
            password='pass08'  # 適切なパスワードを設定
        )

        if connection.is_connected():
            cursor = connection.cursor()

            # SQLクエリの定義
            update_query = """
            UPDATE match_histories
            SET rating = %s, review = %s
            WHERE history_id = %s
            """

            # データをタプルにして準備
            data_tuple = (rating, review, history_id)

            # SQLクエリを実行
            cursor.execute(update_query, data_tuple)
            connection.commit()

            print(f"Match history updated successfully: {cursor.rowcount} row(s) affected")
            return True

    except Error as e:
        print(f"Error while connecting to MySQL: {e}")
        return False

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

# 関数の使用例
'''
result = update_match_history(1, 5, "Excellent match")
print("Success" if result else "Failed")
'''


def get_match_history(history_id):
    try:
        # データベース接続の設定
        connection = mysql.connector.connect(
            host='localhost',  # 適切なホスト名を設定
            database='MATCHINGAPP',  # 適切なデータベース名を設定
            user='team08',  # 適切なユーザー名を設定
            password='pass08'  # 適切なパスワードを設定
        )

        if connection.is_connected():
            cursor = connection.cursor()

            # SQLクエリの定義
            select_query = """
            SELECT match_date, student_id, teacher_id, rating, review
            FROM match_histories
            WHERE history_id = %s
            """

            # データをタプルにして準備
            cursor.execute(select_query, (history_id,))

            # 結果をフェッチ
            record = cursor.fetchone()

            if record:
                return list(record)
            else:
                print(f"No record found with history_id: {history_id}")
                return None

    except Error as e:
        print(f"Error while connecting to MySQL: {e}")
        return None

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

# 関数の使用例
'''
history = get_match_history(1)
if history:
    print("Match History:", history)
else:
    print("No history found or error occurred")
'''