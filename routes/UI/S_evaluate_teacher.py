# routes/UI/S_evaluate_teacher.py

from flask import Blueprint, render_template, session, redirect, url_for
from routes.review.pickup_teacher import get_teacher_ids, get_teacher_names

evaluate_bp = Blueprint('evaluate', __name__)

@evaluate_bp.route('/S_evaluate_teacher')
def S_evaluate_teacher():
    student_id = session.get('id')  # セッションからstudent_idを取得
    if student_id is None:
        print("Student ID is not in session.")  # デバッグ用ログ出力
        # ログインしていない場合の処理
        return redirect(url_for('login.login'))  # ログインページにリダイレクト

    print("Student ID in session:", student_id)  # デバッグ用ログ出力

    teacher_ids = get_teacher_ids(student_id)
    print("Teacher IDs in view:", teacher_ids)  # デバッグ用ログ出力

    teacher_names = get_teacher_names(teacher_ids)
    print("Teacher names in view:", teacher_names)  # デバッグ用ログ出力

    return render_template('S_evaluate_teacher.html', username=session.get('username'), teacher_names=teacher_names)
