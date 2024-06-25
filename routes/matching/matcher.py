from flask import Flask, render_template, request, redirect, url_for, session
import mysql.connector

app = Flask(__name__)
app.secret_key = 'your_secret_key'

def get_db_connection():
    connection = mysql.connector.connect(
        host='localhost',
        user='team08',
        password='pass08',
        database='MatchingApp'
    )
    return connection

@app.route('/match')
def match_students():
    student_id = request.args.get('student_id')
    if not student_id:
        return "Student ID is required", 400

    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)

    cursor.execute('SELECT * FROM student_profiles WHERE id = %s', (student_id,))
    student = cursor.fetchone()

    if not student:
        return "Student not found", 404

    cursor.execute('SELECT * FROM teacher_profiles')
    teachers = cursor.fetchall()

    # マッチングロジック
    matched_teachers = sorted(teachers, key=lambda teacher: (
        teacher['subjects'].split(',').count(student['desired_subject']),  # ①受講希望科目
        len(set(teacher['available_days'].split(',')).intersection(student['available_days'].split(','))),  # ②受講希望曜日
        teacher['gender'] == student['gender']  # ③性別
    ), reverse=True)[:3]

    for teacher in matched_teachers:
        cursor.execute('SELECT * FROM reviews WHERE teacher_id = %s', (teacher['id'],))
        teacher['reviews'] = cursor.fetchall()

    cursor.close()
    connection.close()

    return render_template('matched_teachers.html', student=student, teachers=matched_teachers)

if __name__ == '__main__':
    app.run(debug=True)
