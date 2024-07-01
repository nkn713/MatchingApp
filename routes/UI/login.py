from flask import Blueprint, render_template, request, redirect, url_for, session
from routes.auth.auth import authenticate_user

login_bp = Blueprint('login', __name__)

@login_bp.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']  # 'username' ではなく 'email' として指定されています
        user_type = request.form['user_type']

        # 認証ロジック
        if authenticate_user(email, user_type):
            session['email'] = email
            if user_type == 'student':
                return redirect(url_for('login.student_home'))
            elif user_type == 'teacher':
                return redirect(url_for('login.teacher_home'))
            elif user_type == 'admin':
                return redirect(url_for('login.admin_home'))
        else:
            return "Login Failed. Please check your credentials."

    return render_template('login.html')


@login_bp.route('/student_home')
def student_home():
    if 'email' not in session:
        return redirect(url_for('login.login'))
    return render_template('S_homeview.html', email=session.get('email'))

@login_bp.route('/teacher_home')
def teacher_home():
    if 'email' not in session:
        return redirect(url_for('login.login'))
    return render_template('T_homeview.html', email=session.get('email'))

@login_bp.route('/admin_home')
def admin_home():
    if 'email' not in session:
        return redirect(url_for('login.login'))
    return render_template('A_homeview.html', email=session.get('email'))

@login_bp.route('/register')
def register():
    return render_template('register.html')
