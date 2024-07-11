from flask import Blueprint, request, render_template, redirect, url_for, session, flash
from routes.profile.S_take_attend import insert_preference
from routes.get_info.get_some_id import get_profile_id
from routes.get_info.get_teacher_profiles import get_teacher_profiles

S_take_attend_bp = Blueprint('S_take_attend_bp', __name__)

@S_take_attend_bp.route('/')
def index():
    return render_template('S_take_attend.html')

@S_take_attend_bp.route('/submit_preference', methods=['POST'])
def submit_preference():
    try:
        student_id = get_profile_id(session.get('id'))
        if student_id is None:
            flash('Student ID not found. Please log in again.', 'error')
            return redirect(url_for('S_take_attend_bp.index'))

        subject = request.form['subject']
        day = request.form['day']
        period = request.form['period']

        preference_id, result_message = insert_preference(student_id, subject, day, period)
        session['preference_id'] = preference_id

        # ここでマッチングモジュールを使用。戻り値の講師idをS_select_teacher.pyへ渡す
        teacher_ids = [1, 2, 3]
        teacher_profiles = get_teacher_profiles(teacher_ids)
        return render_template('S_select_teacher.html', username=session.get('username'), teacher_profiles=teacher_profiles, result_message=result_message, preference_id=preference_id)
    except Exception as e:
        print(f'Error in submit_preference: {e}')
        flash('An unexpected error occurred. Please try again later.', 'error')
        return redirect(url_for('S_take_attend_bp.index'))
