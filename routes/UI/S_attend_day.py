from flask import Blueprint, render_template, redirect, url_for, session, request

attend_day_bp = Blueprint('attend_day_bp', __name__)

@attend_day_bp.route('/select_date', methods=['GET', 'POST'])
def select_date():
    if 'username' not in session:
        return redirect(url_for('login.login'))

    if request.method == 'POST':
        # 選択された日時を処理する（この例では実装していません）
        return redirect(url_for('attend_day_bp.select_subject'))

    return render_template('S_attend_day.html', username=session.get('username'))

@attend_day_bp.route('/select_subject', methods=['GET', 'POST'])
def select_subject():
    if 'username' not in session:
        return redirect(url_for('login.login'))

    if request.method == 'POST':
        # 選択された科目を処理する（この例では実装していません）
        return redirect(url_for('S_select_teacher_bp.select_teacher'))

    return render_template('S_take_subject.html')

# 次へ、戻る、ログアウトボタンの処理を行う関数例

@attend_day_bp.route('/next', methods=['POST'])
def handle_next():
    # '次へ' ボタンが押された時の処理を行う
    return redirect(url_for('attend_day_bp.select_subject'))

@attend_day_bp.route('/back', methods=['POST'])
def handle_back():
    # '戻る' ボタンが押された時の処理を行う
    return redirect(url_for('homeview_bp.student_home'))

@attend_day_bp.route('/logout', methods=['POST'])
def handle_logout():
    # 'ログアウト' ボタンが押された時の処理を行う（logout_bpのlogoutエンドポイントにリダイレクトする）
    return redirect(url_for('logout_bp.logout'))

