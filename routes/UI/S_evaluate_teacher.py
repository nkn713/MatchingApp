from flask import Blueprint, redirect, url_for, session, render_template

evaluate_bp = Blueprint('evaluate', __name__)

@evaluate_bp.route('/evaluate_teacher')
def evaluate_teacher():
    if 'username' not in session:
        return redirect(url_for('login.login'))

    # テスト用のデータを挿入
    teachers = [
        {'id': 1, 'name': 'Teacher A', 'photo_url': 'https://example.com/photo1.jpg'},
        {'id': 2, 'name': 'Teacher B', 'photo_url': 'https://example.com/photo2.jpg'},
        {'id': 3, 'name': 'Teacher C', 'photo_url': 'https://example.com/photo3.jpg'}
    ]

    return render_template('S_evaluate_teacher.html', username=session['username'], teachers=teachers)

@evaluate_bp.route('/previous_page')
def previous_page():
    return redirect(url_for('homeview_bp.student_home'))
