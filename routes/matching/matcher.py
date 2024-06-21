# matching/matcher.py

import mysql.connector
from collections import defaultdict

# データベース接続の設定
db_config = {
    'user': 'team08',
    'password': 'pass08',
    'host': 'localhost',
    'database': 'MatchingApp'
}

# データベースに接続する
conn = mysql.connector.connect(**db_config)
cursor = conn.cursor(dictionary=True)

def get_students():
    cursor.execute("SELECT * FROM Students")
    return cursor.fetchall()

def get_teachers():
    cursor.execute("SELECT * FROM Teachers")
    return cursor.fetchall()

def match_students_to_teachers(students, teachers):
    matches = defaultdict(list)

    for student in students:
        potential_teachers = []

        for teacher in teachers:
            score = 0
            # 1. 生徒の受講希望科目と講師の教務可能科目
            if student['preferred_subject'] in teacher['subjects']:
                score += 3
            # 2. 生徒の受講希望曜日と講師の出勤可能曜日
            student_days = set(student['preferred_days'].split(','))
            teacher_days = set(teacher['available_days'].split(','))
            if not student_days.isdisjoint(teacher_days):
                score += 2
            # 3. 生徒と講師の性別
            if student['gender'] == teacher['gender']:
                score += 1
            
            if score > 0:
                potential_teachers.append((teacher, score))
        
        # スコア順にソートして上位3人を選出
        potential_teachers.sort(key=lambda x: x[1], reverse=True)
        matches[student['id']] = [t[0] for t in potential_teachers[:3]]
    
    return matches

def display_matches(matches):
    for student_id, teachers in matches.items():
        print(f"Student ID: {student_id}")
        for teacher in teachers:
            print(f"  Teacher ID: {teacher['id']}, Name: {teacher['name']}, Subjects: {teacher['subjects']}")
            cursor.execute("SELECT * FROM Reviews WHERE teacher_id = %s", (teacher['id'],))
            reviews = cursor.fetchall()
            for review in reviews:
                print(f"    Review: {review['review_text']} (Rating: {review['rating']})")
        print()

if __name__ == "__main__":
    students = get_students()
    teachers = get_teachers()
    matches = match_students_to_teachers(students, teachers)
    display_matches(matches)

    # データベース接続を閉じる
    cursor.close()
    conn.close()
