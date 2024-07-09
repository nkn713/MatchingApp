from flask import Blueprint, render_template, session, redirect, url_for, request, flash
from routes.review.pickup_teacher import get_teacher_ids, get_teacher_names
from routes.review.review_register import register_review
from routes.review import mysql

evaluate_bp = Blueprint('evaluate', __name__)

@evaluate_bp.route('/S_evaluate_teacher')
def S_evaluate_teacher():
    student_id = session.get('id')
    if student_id is None:
        return redirect(url_for('login.login'))

    teacher_ids = get_teacher_ids(student_id)
    teacher_names = get_teacher_names(teacher_ids)

    return render_template('S_evaluate_teacher.html', username=session.get('username'), teacher_names=teacher_names)

@evaluate_bp.route('/submit_review/<int:teacher_id>', methods=['POST'])
def submit_review(teacher_id):
    student_id = session.get('id')
    if student_id is None:
        return redirect(url_for('login.login'))

    rating = request.form.get('rating')
    comment = request.form.get('comment')

    if register_review(student_id, teacher_id, rating, comment):
        flash('評価が正常に送信されました。', 'success')
    else:
        flash('評価の送信中にエラーが発生しました。', 'danger')

    return redirect(url_for('evaluate.S_evaluate_teacher'))
