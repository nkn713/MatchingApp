from flask import Blueprint, request, render_template, redirect, url_for
from routes.profile.S_take_attend import insert_or_update_preference

S_take_attend_bp = Blueprint('S_take_attend', __name__)

@S_take_attend_bp.route('/')
def index():
    return render_template('S_take_atted.html')

@S_take_attend_bp.route('/submit_preference', methods=['POST'])
def submit_preference():
    student_id = request.form['student_id']
    subject = request.form['subject']
    day = request.form['day']
    period = request.form['period']

    result = insert_or_update_preference(student_id, subject, day, period)
    return render_template('S_homeview.html', result=result)
