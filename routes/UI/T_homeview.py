from flask import Blueprint, render_template, request, redirect, url_for, session

T_homeview_bp = Blueprint('T_homeview', __name__)

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
        university = request.form['university']
        # プロフィール情報をデータベースに保存するコードを追加します。
        return redirect(url_for('T_homeview_bp.teacher_home'))
    return render_template('T_profile_input.html', username=session.get('username'), form_data={}, errors={})

@T_homeview_bp.route('/T_take_attend', methods=['GET', 'POST'])
def T_take_attend():
    if 'username' not in session:
        return redirect(url_for('login.login'))
    return render_template('T_take_attend.html', username=session.get('username'), id=session.get('id'))

