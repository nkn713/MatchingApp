import mysql.connector

# データベース接続の設定
db_config = {
    'user': 'team08',
    'password': 'pass08',
    'host': 'localhost',
    'database': 'MATCHINGAPP'
}

def insert_preference(student_id, subject, day, period):
    if student_id is None or subject is None or day is None or period is None:
        return None, "エラー: 入力された値のいずれかがNULLです。"

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


def check_student_profile_complete(student_id):
    try:
        # データベースに接続
        conn = mysql.connector.connect(
            host="localhost",      # データベースホスト名
            user="team08",  # データベースユーザ名
            password="pass08",  # データベースパスワード
            database="MATCHINGAPP"   # データベース名
        )
        
        cursor = conn.cursor()
        
        # student_profiles テーブルから指定された student_id のレコードを取得
        query = "SELECT * FROM student_profiles WHERE id = %s"
        cursor.execute(query, (student_id,))
        record = cursor.fetchone()
        
        # レコードが存在しない場合
        if record is None:
            return False
        
        # レコードの各フィールドをチェックしてnullがあるか確認
        for field in record:
            if field is None:
                return False
        
        return True
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return False
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()