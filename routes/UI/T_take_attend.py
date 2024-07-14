from flask import Blueprint, request, render_template, redirect, session, url_for
from routes.profile.T_take_attend import insert_or_update_availability
from routes.get_info.get_some_id import get_profile_id

T_take_attend_bp = Blueprint('T_take_attend', __name__)

@T_take_attend_bp.route('/')
def index():
    return render_template('T_take_attend.html')

@T_take_attend_bp.route('/submit_availability', methods=['GET', 'POST'])
def submit_availability():
    if request.method == 'POST':
        teacher_id = get_profile_id(session.get('id'))
        subjects = request.form.getlist('subjects')
        day = request.form.get('day')
        periods = request.form.getlist('periods')
        username = session.get('username')
        action = request.form.get('action')

        print(f"Received POST data: teacher_id={teacher_id}, subjects={subjects}, day={day}, periods={periods}, action={action}")

        if action == 'button1':
            insert_or_update_availability(teacher_id, subjects, day, periods)
            return render_template('T_take_attend.html', username=username)
        elif action == 'button2':
            result = insert_or_update_availability(teacher_id, subjects, day, periods)
            return render_template('T_homeview.html', result=result, username=username)
    else:
        return redirect(url_for('T_take_attend.index'))

@T_take_attend_bp.route('/T_homeview')
def back_homeview():
    username = session.get('username')
    return render_template('T_homeview.html', username=username)
