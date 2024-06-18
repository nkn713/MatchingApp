from flask import Blueprint, render_template, request, redirect, url_for, session

login_bp = Blueprint('login', __name__)

@login_bp.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user_type = request.form['user_type']

        # 簡易的な認証ロジック
        # どのユーザーネームやパスワードでもログインできるようにする
        session['username'] = username
        if user_type == 'student':
            return redirect(url_for('login.student_home'))
        elif user_type == 'teacher':
            return redirect(url_for('login.teacher_home'))
        elif user_type == 'admin':
            return redirect(url_for('login.admin_home'))
    return render_template('login.html')

@login_bp.route('/student_home')
def student_home():
    if 'username' not in session:
        return redirect(url_for('login.login'))
    return render_template('S_homeview.html', username=session.get('username'))

@login_bp.route('/teacher_home')
def teacher_home():
    if 'username' not in session:
        return redirect(url_for('login.login'))
    return render_template('T_homeview.html', username=session.get('username'))

@login_bp.route('/admin_home')
def admin_home():
    if 'username' not in session:
        return redirect(url_for('login.login'))
    return render_template('A_homeview.html', username=session.get('username'))

@login_bp.route('/register')
def register():
    return render_template('register.html')