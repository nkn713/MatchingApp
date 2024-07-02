<<<<<<< HEAD
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('student_prof.html')

if __name__ == "__main__":
    app.run(debug=True)
=======
from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from routes.profile.profile_service import process_student_profile
from routes.profile.error_handling import ValidationError, handle_error
from routes.profile.database_operations import mysql

S_profile_input_bp = Blueprint('S_profile_input', __name__)

@S_profile_input_bp.route('/student_home')
def student_home():
    return render_template('S_homeview.html', username=session.get('username'))

@S_profile_input_bp.route('/profile')
def profile():
    return render_template('S_profile_input.html', username=session.get('username'), form_data={}, errors={})

@S_profile_input_bp.route('/S_profile_input', methods=['POST'])
def S_profile_input():
    email = session.get('email')
    if not email:
        flash('セッションにメールアドレスがありません。再度ログインしてください。', 'error')
        return redirect(url_for('register.login'))

    name = request.form['name']
    gender = request.form['gender']
    affiliation = request.form['affiliation']
    grade = request.form['grade']
    session['name'] = name
    session['gender'] = gender
    session['affiliation'] = affiliation
    session['grade'] = grade
    form_data = {
        'email': email,
        'name': name,
        'gender': gender,
        'affiliation': affiliation,
        'grade': grade
    }

    errors = {}

    try:
        process_student_profile(email, name, gender, affiliation, grade)
        flash('プロフィールが正常に保存されました。', 'success')
        return redirect(url_for('S_profile_input.student_home'))
    except ValidationError as error:
        message, category, field_name = handle_error(error)
        errors[field_name] = message
        return render_template('S_profile_input.html', username=session.get('username'), form_data=form_data, errors=errors)
    except Exception as e:
        flash('予期しないエラーが発生しました。', 'error')
        return render_template('S_profile_input.html', username=session.get('username'), form_data=form_data, errors={})
>>>>>>> b51f2a9bc66494a62777f80fe89a198d7948be7c
