from flask import render_template, Blueprint, request, redirect, url_for, session
from routes.select.select_teacher import get_teacher_profile, insert_match_status
from routes.select.send_emails import send_match_emails
from routes.history.match_history import insert_match_history
from routes.get_info.get_some_id import get_profile_id

S_select_teacher_bp = Blueprint('S_select_teacher', __name__)

@S_select_teacher_bp.route('/confirm', methods=['GET','POST'])
def confirm():
    error = None
    if request.method == 'POST':
        # ログイン情報から生徒idを取得してinser_match_statusの第一引数に代入
        student_id = get_profile_id(session.get('id'))
        teacher_id = request.form.get('teacher_id')  # 安全に取得
        if not teacher_id:
            error = "ラジオボタンを選択してください"
        else:
            match_id = insert_match_status(student_id, teacher_id)
            history = insert_match_history(student_id, teacher_id)
            return render_template('S_homeview.html', username=session.get('username'), match_id=match_id, history=history)
    return render_template('S_select_teacher.html', error=error)

@S_select_teacher_bp.route('/back')
def back():
    return render_template('S_take_attend.html', username=session.get('username'))

@S_select_teacher_bp.route('/S_select_teacher')
def S_select_teacher():
    return render_template('S_select_teacher.html')
