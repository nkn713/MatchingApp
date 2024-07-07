import mysql.connector

#マッチングの条件は以下の通り
#・生徒の男性女性希望＆講師の性別
#・生徒の「運動部」or「文化部」or「その他」＆講師の学生時代の所属部活が「運動部」か「文化部」か「その他」
#・生徒の所属する学校（私立or国公立、その他)＆講師のかつて所属していた学校の区分（公立か私立）
#※小学生生徒の場合は無視
#※中学生・高校生の所属学校（私立or国公立、その他)に対して講師の中学校区分（公立か私立）
#生徒が「私立」の場合は講師の中学校区分「私立」と、生徒が「国公立」の場合は講師の中学校区分「公立」とマッチングさせる。
#生徒が「その他」を選択した場合はどちらでもよいことにする
#・生徒の志望校のレベル（偏差値)＆講師の偏差値（数字で入力）
#※偏差値の分け方を55以下、56~60、61~65、66以上
#・生徒の受講目的（受験or学校補習）＆講師の受験経験
#※講師の中学受験の有無　（小学生対象）
#※講師の国公立高校の受験経験の有無、私立高校の受験経験の有無（中学生対象）
#※講師の国公立大学の受験経験の有無、私立大学の受験経験の有無（高校生対象）
#・生徒の受講目的（受験or学校補習）＆講師の得意とする授業スタイル（学校補習メインか受験対策メインか）

def get_db_connection():
    connection = mysql.connector.connect(
        host='localhost',
        user='team08',
        password='pass08',
        database='MatchingApp'
    )
    return connection

def fetch_student_profile(student_id):
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute('SELECT * FROM student_profiles WHERE id = %s', (student_id,))
    student_profile = cursor.fetchone()
    cursor.close()
    connection.close()
    return student_profile

def fetch_teacher_profiles():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute('SELECT * FROM teacher_profiles')
    teacher_profiles = cursor.fetchall()
    cursor.close()
    connection.close()
    return teacher_profiles

def calculate_match_score(student, teacher):
    score = 0

    # 性別の希望
    if student['preferred_gender'] == teacher['gender']:
        score += 1

    # 部活動
    if student['club_activity'] == teacher['club_activities']:
        score += 1

    # 学校区分
    if student['grade'] > 6:
        if student['school_type'] == '私立' and teacher['middle_school_type'] == '私立':
            score += 1
        elif student['school_type'] == '国公立' and teacher['middle_school_type'] == '公立':
            score += 1
        elif student['school_type'] == 'その他':
            score += 1

    # 偏差値
    if (student['target_school_level'] <= 55 and teacher['deviation_value'] <= 55) or \
       (56 <= student['target_school_level'] <= 60 and 56 <= teacher['deviation_value'] <= 60) or \
       (61 <= student['target_school_level'] <= 65 and 61 <= teacher['deviation_value'] <= 65) or \
       (66 <= student['target_school_level'] and 66 <= teacher['deviation_value']):
        score += 1

    # 受講目的と講師の経験
    if student['purpose'] == '受験':
        if (student['grade'] <= 6 and teacher['exam_experience'].find('中学受験') != -1) or \
           (7 <= student['grade'] <= 9 and (teacher['exam_experience'].find('国公立高校受験') != -1 or teacher['exam_experience'].find('私立高校受験') != -1)) or \
           (10 <= student['grade'] and (teacher['exam_experience'].find('国公立大学受験') != -1 or teacher['exam_experience'].find('私立大学受験') != -1)):
            score += 1

    # 受講目的と講師の得意なスタイル
    if student['purpose'] == '学校補習' and teacher['teaching_style'] == '学校補習メイン':
        score += 1
    elif student['purpose'] == '受験' and teacher['teaching_style'] == '受験対策メイン':
        score += 1

    return score

def find_best_teachers(student_id):
    student = fetch_student_profile(student_id)
    teachers = fetch_teacher_profiles()
    
    matches = []
    for teacher in teachers:
        score = calculate_match_score(student, teacher)
        matches.append((teacher['id'], score))
    
    matches = sorted(matches, key=lambda x: x[1], reverse=True)
    return [teacher_id for teacher_id, score in matches[:3]]

#テスト用？
def main():
    student_id = 1  # Example student ID
    top_teachers = find_best_teachers(student_id)
    
    print("Top 3 matching teacher IDs:")
    for teacher_id in top_teachers:
        print(f"Teacher ID: {teacher_id}")

if __name__ == '__main__':
    main()
