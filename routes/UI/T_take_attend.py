from flask import Blueprint, request, render_template, redirect, session, url_for
from routes.profile.T_take_attend import insert_or_update_availability
from routes.get_info.get_some_id import get_profile_id

T_take_attend_bp = Blueprint('T_take_attend_bp', __name__)

@T_take_attend_bp.route('/', methods=['GET'])
def index():
    return render_template('T_take_attend.html', errors={}, username=session.get('username'))

@T_take_attend_bp.route('/submit_availability', methods=['POST'])
def submit_availability():
    errors = {}
    teacher_id = get_profile_id(session.get('id'))
    subjects = request.form.getlist('subjects')
    days = request.form.getlist('days')
    periods = request.form.getlist('periods')
    username = session.get('username')
    action = request.form.get('action')

    # バリデーションの例
    if not subjects:
        errors['subjects'] = '少なくとも1つの科目を選択してください。'
    if not days:
        errors['days'] = '少なくとも1つの曜日を選択してください。'
    if not periods:
        errors['periods'] = '少なくとも1つの時限を選択してください。'

    if errors:
        return render_template('T_take_attend.html', errors=errors, username=username)

    try:
        if action == 'button1':
            insert_or_update_availability(teacher_id, subjects, days, periods)
            return render_template('T_take_attend.html', username=username, errors={})
        elif action == 'button2':
            result = insert_or_update_availability(teacher_id, subjects, days, periods)
            return render_template('T_homeview.html', result=result, username=username)
    except Exception as e:
        errors['form'] = 'データベース処理中にエラーが発生しました。'
        return render_template('T_take_attend.html', errors=errors, username=username)

@T_take_attend_bp.route('/T_homeview', methods=['GET'])
def back_homeview():
    username = session.get('username')
    return render_template('T_homeview.html', username=username)
