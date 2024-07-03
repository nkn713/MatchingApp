from flask import Blueprint, render_template, request, redirect, url_for, session

register_bp = Blueprint('register',__name__)
#追加
from flask_mysqldb import MySQL 
from flask import current_app
from routes.signUp.signup import RegisterToDatabase
#追加

register_bp = Blueprint('register', __name__)

@register_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user_type = request.form['user_type']
        username = request.form['username'] 
        RegisterToDatabase(password,email,user_type,username)
        session['email'] = email
        session['password'] = password
        # ここで新規登録処理を実行する
        return redirect(url_for('register.success'))
    return render_template('register.html')

#ログイン画面と新規登録画面に戻る遷移になっているはす
@register_bp.route('/success')
def success():
    if 'email' in session:
        if 'password' in session:
            return render_template('login.html')
    return render_template('register.html')

@register_bp.route('/login')
def login():
    return render_template('login.html')

