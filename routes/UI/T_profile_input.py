from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from routes.profile.profile_service import process_teacher_profile
from routes.profile.error_handling import ValidationError, handle_error
from routes.profile.database_operations import mysql

T_profile_input_bp = Blueprint('T_profile_input', __name__)

@T_profile_input_bp.route('/teacher_home')
def teacher_home():
    return render_template('T_homeview.html', username=session.get('username'))

@T_profile_input_bp.route('/profile')
def profile():
    return render_template('T_profile_input.html', username=session.get('username'), form_data={}, errors={})

@T_profile_input_bp.route('/T_profile_input', methods=['POST'])
def T_profile_input():
    email = session.get('email')
    if not email:
        flash('セッションにメールアドレスがありません。再度ログインしてください。', 'error')
        return redirect(url_for('login'))  # 修正: 'register.login' から 'login' に変更

    name = request.form['name']
    gender = request.form['gender']
    affiliation = request.form['affiliation']
    university = request.form['university']
    session['name'] = name
    session['gender'] = gender
    session['affiliation'] = affiliation
    session['university'] = university
    form_data = {
        'email': email,
        'name': name,
        'gender': gender,
        'affiliation': affiliation,
        'university': university
    }

    errors = {}

    try:
        process_teacher_profile(email, name, gender, affiliation, university)
        flash('プロフィールが正常に保存されました。', 'success')
        return redirect(url_for('T_profile_input.teacher_home'))
    except ValidationError as error:
        message, category, field_name = handle_error(error)
        errors[field_name] = message
        return render_template('T_profile_input.html', username=session.get('username'), form_data=form_data, errors=errors)
    except Exception as e:
        flash('予期しないエラーが発生しました。', 'error')
        return render_template('T_profile_input.html', username=session.get('username'), form_data=form_data, errors={})
