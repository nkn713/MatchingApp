from flask import render_template, Blueprint, request, redirect, url_for, session
from routes.select.select_teacher import get_teacher_profile, insert_match_status
from routes.select.send_emails import send_match_emails
from routes.history.match_history import insert_match_history

S_select_teacher_bp = Blueprint('S_select_teacher', __name__)

@S_select_teacher_bp.route('/confirm', methods=['GET','POST'])
def confirm():
    if request.method == 'POST':
        #ログイン情報から生徒idを取得してinser_match_statusの第一引数に代入
        student_id = session.get('id')
        teacher_id = 1
        match_id = insert_match_status(student_id, teacher_id)
        history_id = insert_match_history(student_id, teacher_id)
        return render_template('S_homeview.html', username=session.get('username'), match_id=match_id, history_id=history_id)
    return render_template('S_select_teacher.html')

@S_select_teacher_bp.route('/back')
def back():
    return render_template('S_take_attend.html', username=session.get('username'))


@S_select_teacher_bp.route('/S_select_teacher')
def S_select_teacher():
    return render_template('S_select_teacher.html')

