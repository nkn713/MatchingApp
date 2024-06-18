from flask import Blueprint, render_template, request, redirect, url_for, session

T_homeview_bp = Blueprint('T_homeview_bp', __name__)

@T_homeview_bp.route('/teacher_home')
def teacher_home():
    if 'username' not in session:
        return redirect(url_for('login.login'))
    return render_template('T_homeview.html', username=session.get('username'))

@T_homeview_bp.route('/profile', methods=['GET', 'POST'])
def profile():
    if 'username' not in session:
        return redirect(url_for('login.login'))
    if request.method == 'POST':
        name = request.form['name']
        gender = request.form['gender']
        affiliation = request.form['affiliation']
        grade = request.form['grade']
        # プロフィール情報をデータベースに保存するコードを追加します。
        return redirect(url_for('T_homeview_bp.teacher_home'))
    return render_template('T_profile_input.html')

@T_homeview_bp.route('/select_date', methods=['GET', 'POST'])
def select_date():
    if 'username' not in session:
        return redirect(url_for('login.login'))
    if request.method == 'POST':
        # 日時選択の処理を追加します
        return redirect(url_for('T_homeview_bp.select_subject'))
    return render_template('T_attend_day.html')

@T_homeview_bp.route('/select_subject', methods=['GET', 'POST'])
def select_subject():
    if 'username' not in session:
        return redirect(url_for('login.login'))
    if request.method == 'POST':
        # 科目選択の処理を追加します
        return redirect(url_for('T_homeview_bp.select_date'))
    return render_template('T_take_subject.html')
