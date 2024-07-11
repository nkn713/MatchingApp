from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from routes.profile.profile_service1 import process_student_profile
from routes.profile.error_handling import ValidationError, handle_error

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
    name = session.get('name')  # セッションから名前を取得
    if not email:
        flash('セッションにメールアドレスがありません。再度ログインしてください。', 'error')
        return redirect(url_for('register.login'))
    if not name:
        flash('セッションに名前がありません。再度ログインしてください。', 'error')
        return redirect(url_for('register.login'))

    try:
        gender = request.form['gender']
        preferred_gender = request.form['preference']
        purpose = request.form['learning_purpose']
        target_school_level = request.form['desired_school_level']
        club_activity = request.form['club_activity']
        school_type = request.form['school_type']
        print(f"Form Data: {request.form}")  # ここでフォームデータを出力して確認する
    except KeyError as e:
        flash(f'フォームに不足しているフィールドがあります: {e}', 'error')
        return redirect(url_for('S_profile_input.profile'))

    session['gender'] = gender
    form_data = {
        'email': email,
        'name': name,
        'gender': gender,
        'preferred_gender': preferred_gender,
        'purpose': purpose,
        'target_school_level': target_school_level,
        'club_activity': club_activity,
        'school_type': school_type
    }

    errors = {}

    try:
        process_student_profile(email, name, gender, preferred_gender, purpose, target_school_level, club_activity, school_type)
        flash('プロフィールが正常に保存されました。', 'success')
        return redirect(url_for('S_profile_input.student_home'))
    except ValidationError as error:
        message, category, field_name = handle_error(error)
        errors[field_name] = message
        return render_template('S_profile_input.html', username=session.get('username'), form_data=form_data, errors=errors)
    except Exception as e:
        flash(f'予期しないエラーが発生しました: {e}', 'error')
        return render_template('S_profile_input.html', username=session.get('username'), form_data=form_data, errors={})
