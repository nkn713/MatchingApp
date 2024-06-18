from flask import render_template, Blueprint, request, redirect, url_for

S_select_teacher_bp = Blueprint('S_select_teacher', __name__)

@S_select_teacher_bp.route('/confirm', methods=['GET','POST'])
def confirm():
    if request.method == 'POST':
        return render_template('S_homeview.html')
    return render_template('S_select_teacher.html')

@S_select_teacher_bp.route('/back')
def back():
    return render_template('S_take_subject.html')


@S_select_teacher_bp.route('/S_select_teacher')
def S_select_teacher():
    return render_template('S_select_teacher.html')

