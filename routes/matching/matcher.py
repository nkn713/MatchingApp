import mysql.connector
import unittest

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
    if student_profile is None:
        raise ValueError(f"Student with ID {student_id} not found.")
    return student_profile

def fetch_teacher_profiles():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute('SELECT * FROM teacher_profiles')
    teacher_profiles = cursor.fetchall()
    cursor.close()
    connection.close()
    return teacher_profiles

def fetch_student_preferences(student_id):
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute('SELECT * FROM student_preferences WHERE student_id = %s', (student_id,))
    preferences = cursor.fetchall()
    cursor.close()
    connection.close()
    return preferences

def fetch_teacher_preferences(teacher_id):
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute('SELECT * FROM teacher_preferences WHERE teacher_id = %s', (teacher_id,))
    preferences = cursor.fetchall()
    cursor.close()
    connection.close()
    return preferences

def calculate_match_score(student, teacher):
    target_school_level = int(student['target_school_level'])

    deviation_value = teacher.get('deviation_value', 0)
    if deviation_value is None:
        deviation_value = 0
    else:
        deviation_value = int(deviation_value)

    if target_school_level <= deviation_value:
        score = 1
    else:
        score = 0

    return score

def find_best_teachers(student_id):
    try:
        student = fetch_student_profile(student_id)
        student_prefs = fetch_student_preferences(student_id)
        teachers = fetch_teacher_profiles()
        
        print(f"Student: {student}")
        print(f"Student Preferences: {student_prefs}")
        print(f"Teachers: {teachers}")

        matches = []
        for teacher in teachers:
            teacher_prefs = fetch_teacher_preferences(teacher['id'])
            
            print(f"Checking teacher: {teacher['id']}")
            print(f"Teacher Preferences: {teacher_prefs}")

            # 教師のPreferencesが空の場合は除外
            if not teacher_prefs:
                continue

            score = 0
            for student_pref in student_prefs:
                found_preference = False
                for teacher_pref in teacher_prefs:
                    if (student_pref['subject'] == teacher_pref['subject'] and 
                        student_pref['preferred_day'] == teacher_pref['preferred_day'] and 
                        student_pref['preferred_period'] == teacher_pref['preferred_period']):
                        found_preference = True
                        score += 1  # 完全一致でスコアを増加
                        break
                if not found_preference:
                    # 部分一致でもスコアを増加させる（例：subjectの一致）
                    for teacher_pref in teacher_prefs:
                        if student_pref['subject'] == teacher_pref['subject']:
                            score += 0.5  # 部分一致でスコアを少し増加
                            break

            # スコアに教師の他の要素を加味
            score += calculate_match_score(student, teacher)

            matches.append((teacher['id'], score))

        matches = sorted(matches, key=lambda x: x[1], reverse=True)
        print(f"Matches found: {matches}")
        return [teacher_id for teacher_id, score in matches]
    except Exception as e:
        print(f"Error in find_best_teachers: {e}")
        return []




class TestMatcher(unittest.TestCase):
    
    def test_find_best_teachers(self):
        student_id = 16  # Example student ID
        result = find_best_teachers(student_id)
        print(f"Matching result: {result}")
        self.assertGreater(len(result), 0, f"Expected at least one match, but got {len(result)}.")

if __name__ == '__main__':
    unittest.main()