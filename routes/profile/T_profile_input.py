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

#@app.route('/T_profile_input', methods=['GET', 'POST'])
def T_profile_input():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')
        gender = request.form.get('gender')
        exam_experience = ','.join([
            '中学受験' if request.form.get('middle_school_exam') else '',
            '国公立高校受験' if request.form.get('public_high_school_exam') else '',
            '私立高校受験' if request.form.get('private_high_school_exam') else '',
            '国公立大学受験' if request.form.get('public_university_exam') else '',
            '私立大学受験' if request.form.get('private_university_exam') else ''
        ]).strip(',')
        deviation_value = request.form.get('deviation_value')
        club_activities = request.form.get('club_activity')
        middle_school_type = request.form.get('middle_school_type')
        teaching_style = request.form.get('teaching_style')

        connection = get_db_connection()
        cursor = connection.cursor()

        cursor.execute('''
            INSERT INTO teacher_profiles (name, email, password, gender, exam_experience, deviation_value, club_activities, middle_school_type, teaching_style)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        ''', (name, email, password, gender, exam_experience, deviation_value, club_activities, middle_school_type, teaching_style))

        connection.commit()
        cursor.close()
        connection.close()

        return redirect(url_for('home'))

    return render_template('T_profile_input.html', form_data={}, errors={})

if __name__ == '__main__':
    app.run(debug=True)
