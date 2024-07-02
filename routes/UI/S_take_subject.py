from flask import Blueprint, render_template, redirect, url_for, session, request

take_subject_bp = Blueprint('take_subject_bp', __name__)

@take_subject_bp.route('/select_subject', methods=['GET', 'POST'])
def select_subject():
    if 'username' not in session:
        return redirect(url_for('login.login'))

    if request.method == 'POST':
        action = request.form.get('form_action')

        if action == 'complete':
            # 完了ボタンが押された場合の処理（必要に応じてロジックを追加）
            return redirect(url_for('S_select_teacher_bp.select_teacher'))
        elif action == 'back':
            return redirect(url_for('attend_day_bp.select_date'))

    return render_template('S_take_subject.html')

@take_subject_bp.route('/handle_action', methods=['POST'])
def handle_action():
    action = request.form.get('form_action')

    if action == 'complete':
        # 完了ボタンが押された場合の処理（必要に応じてロジックを追加）
        return redirect(url_for('S_select_teacher_bp.select_teacher'))
    elif action == 'back':
        return redirect(url_for('attend_day_bp.select_date'))

    # 他のアクションの処理が必要な場合はここで追加する

    return redirect(url_for('take_subject_bp.select_subject'))

