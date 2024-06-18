from flask import Blueprint, render_template, redirect, url_for, session

T_take_subject_bp = Blueprint('T_take_subject_bp', __name__)

@T_take_subject_bp.route('/take_subject')
def take_subject():
    if 'username' not in session:
        return redirect(url_for('login.login'))
    return render_template('T_take_subject.html', username=session.get('username'))

@T_take_subject_bp.route('/take_subject/back')
def back():
    return redirect(url_for('T_attend_day_bp.attend_day'))

@T_take_subject_bp.route('/take_subject/complete')
def complete():
    return redirect(url_for('T_homeview_bp.teacher_home'))

@T_take_subject_bp.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login.login'))
