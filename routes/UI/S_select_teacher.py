from flask import render_template, Blueprint, request, redirect, url_for
<<<<<<< HEAD
=======
from routes.select.select_teacher import get_teacher_profile, insert_match_status
from routes.select.send_emails import send_match_emails
>>>>>>> b51f2a9bc66494a62777f80fe89a198d7948be7c

S_select_teacher_bp = Blueprint('S_select_teacher', __name__)

@S_select_teacher_bp.route('/confirm', methods=['GET','POST'])
def confirm():
    if request.method == 'POST':
<<<<<<< HEAD
=======
        #ログイン情報から生徒emailを取得してinser_match_statusの第一引数に代入
        #get_teacher_profileからteacher_emailを取得してinser_match_statusの第二引数に代入
        #teacher_email = get_teacher_profile(teacher_id)['email']
        match_id = insert_match_status('yuusei0625@icloud.com', 'moritsuo@icloud.com')
        send_match_emails(match_id)
>>>>>>> b51f2a9bc66494a62777f80fe89a198d7948be7c
        return render_template('S_homeview.html')
    return render_template('S_select_teacher.html')

@S_select_teacher_bp.route('/back')
def back():
    return render_template('S_take_subject.html')


@S_select_teacher_bp.route('/S_select_teacher')
def S_select_teacher():
    return render_template('S_select_teacher.html')

<<<<<<< HEAD
    
=======
>>>>>>> b51f2a9bc66494a62777f80fe89a198d7948be7c
