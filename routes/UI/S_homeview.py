from flask import Blueprint, render_template, request, redirect, url_for, session

homeview_bp = Blueprint('homeview_bp', __name__)

@homeview_bp.route('/student_home')
def student_home():
    if 'username' not in session:
        return redirect(url_for('login.login'))
    return render_template('S_homeview.html', username=session.get('username'))

@homeview_bp.route('/profile', methods=['GET', 'POST'])
def profile():
    if 'username' not in session:
        return redirect(url_for('login.login'))
    if request.method == 'POST':
        name = request.form['name']
        gender = request.form['gender']
        affiliation = request.form['affiliation']
        grade = request.form['grade']
        # プロフィール情報をデータベースに保存するコードを追加します。
        return redirect(url_for('homeview_bp.student_home'))
    return render_template('S_profile_input.html')

@homeview_bp.route('/select_date', methods=['GET', 'POST'])
def select_date():
    if 'username' not in session:
        return redirect(url_for('login.login'))
    return render_template('S_profile_input.html', username=session.get('username'), form_data={}, errors={})

@homeview_bp.route('/select_date', methods=['GET', 'POST'])
def select_date():
    #if 'username' not in session:
    #    return redirect(url_for('login.login'))
    if request.method == 'POST':
        # 日時選択の処理を追加します
        return redirect(url_for('homeview_bp.select_subject'))
    return render_template('S_attend_day.html')

@homeview_bp.route('/select_subject', methods=['GET', 'POST'])
def select_subject():
    if 'username' not in session:
        return redirect(url_for('login.login'))
    if request.method == 'POST':
        # 科目選択の処理を追加します
        return redirect(url_for('homeview_bp.select_teacher'))
    return render_template('S_take_subject.html')

@homeview_bp.route('/select_teacher', methods=['GET', 'POST'])
def select_teacher():
    if 'username' not in session:
        return redirect(url_for('login.login'))
    if request.method == 'POST':
        # 講師選択の処理を追加します
        return redirect(url_for('homeview_bp.student_home'))
    return render_template('S_select_teacher.html')
