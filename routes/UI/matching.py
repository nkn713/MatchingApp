from flask import Blueprint, render_template, session, redirect, url_for
import mysql.connector

matching_bp = Blueprint('matching_bp', __name__)

# データベース接続の設定
db_config = {
    'user': 'team08',
    'password': 'pass08',
    'host': 'localhost',
    'database': 'MATCHINGAPP'
}

@matching_bp.route('/match_students_and_teachers')
def match_students_and_teachers():
    if 'username' not in session:
        return redirect(url_for('login.login'))

    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor(dictionary=True)

    # 学生と教師のデータを取得
    cursor.execute("SELECT * FROM student_profiles WHERE club_activity = '運動部' AND purpose = '受験'")
    students = cursor.fetchall()

    cursor.execute("SELECT * FROM teacher_profile WHERE club_activity = '運動部' AND teaching_style = '受験対策メイン'")
    teachers = cursor.fetchall()

    conn.close()

    # マッチング結果を格納するリスト
    matches = []

    for student in students:
        for teacher in teachers:
            if student['preferred_gender'] == teacher['gender']:
                matches.append({
                    'teacher_id': teacher['id'],
                    'teacher_name': teacher['name'],
                    'teacher_introduction': teacher['introduction']
                })

    return render_template('matching_results.html', matches=matches, username=session.get('username'))
