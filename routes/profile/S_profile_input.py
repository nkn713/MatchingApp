from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL

app = Flask(__name__)
app.secret_key = 'your_secret_key'

mysql = MySQL()

#@app.route('/S_profile_input', methods=['GET', 'POST'])
def S_profile_input():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')
        gender = request.form.get('gender')
        preferred_gender = request.form.get('preference')
        purpose = request.form.get('learning_purpose')
        target_school_level = request.form.get('desired_school_level')
        club_activity = request.form.get('club_activity')
        school_type = request.form.get('school_type')

        cur = mysql.connection.cursor()
        cur.execute('''
            INSERT INTO student_profiles (name, email, password, gender, preferred_gender, purpose, target_school_level, club_activity, school_type)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        ''', (name, email, password, gender, preferred_gender, purpose, target_school_level, club_activity, school_type))

        mysql.connection.commit()
        cur.close()

        return redirect(url_for('home'))

    return render_template('S_profile_input.html', form_data={}, errors={})

if __name__ == '__main__':
    app.run(debug=True)
