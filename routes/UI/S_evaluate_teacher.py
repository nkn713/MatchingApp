from flask import Blueprint, redirect, url_for, session, render_template

evaluate_bp = Blueprint('evaluate', __name__)

@evaluate_bp.route('/S_evaluate_teacher')
def S_evaluate_teacher():
    return render_template('S_evaluate_teacher.html', username=session.get('username'))

