# routes/UI/S_evaluate_teacher.py

from flask import Blueprint, render_template, session
from routes.review.pickup_teacher import get_teacher_ids, get_teacher_names

evaluate_bp = Blueprint('evaluate', __name__)

@evaluate_bp.route('/S_evaluate_teacher')
def S_evaluate_teacher():
    student_id = session.get('student_id')  # Assuming you store student_id in session
    if student_id is None:
        # Handle case where student is not logged in or session expired
        return redirect(url_for('login.login'))  # Redirect to login page

    teacher_ids = get_teacher_ids(student_id)
    teacher_names = get_teacher_names(teacher_ids)

    return render_template('S_evaluate_teacher.html', username=session.get('username'), teacher_names=teacher_names)
