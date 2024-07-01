from flask import render_template, Blueprint, request, redirect, url_for
from routes.select.select_teacher import get_teacher_profile, insert_match_status
from routes.select.send_match_emails import send_match_emails

S_select_teacher_bp = Blueprint('S_select_teacher', __name__)

@S_select_teacher_bp.route('/confirm', methods=['GET','POST'])
def confirm():
    if request.method == 'POST':
        match_id = insert_match_status('yuusei0625@icloud.com', 'moritsuo@icloud.com')
        send_match_emails(match_id)
        return render_template('S_homeview.html')
    return render_template('S_select_teacher.html')

@S_select_teacher_bp.route('/back')
def back():
    return render_template('S_take_subject.html')


@S_select_teacher_bp.route('/S_select_teacher')
def S_select_teacher():
    return render_template('S_select_teacher.html')

