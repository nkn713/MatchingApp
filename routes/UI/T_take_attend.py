from flask import Blueprint, request, render_template, render_template, redirect, session, url_for
from routes.profile.T_take_attend import insert_or_update_availability

T_take_attend_bp = Blueprint('T_take_attend', __name__)

@T_take_attend_bp.route('/')
def index():
    return render_template('T_take_attend.html')

@T_take_attend_bp.route('/submit_availability', methods=['POST'])
def submit_availability():
    teacher_id = request.form['teacher_id']
    subjects = request.form.getlist('subjects')
    days = request.form.getlist('days')
    periods = request.form.getlist('periods')

    result = insert_or_update_availability(teacher_id, subjects, days, periods)
    return render_template('T_homeview.html', result=result)
