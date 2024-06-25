from flask import Blueprint, render_template, request, redirect, url_for, session
#追加
from flask_mysqldb import MySQL 
from flask import current_app
#追加

register_bp = Blueprint('register', __name__)

#追加
mysql = MySQL()
#

@register_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user_type = request.form['user_type']
        # ここで新規登録処理を実行する

        #追加
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO login (password, email, user_type) VALUES (%s, %s, %s)", (password, email, user_type))
        mysql.connection.commit()
        cur.close()
        #追加
        return redirect(url_for('register.login'))

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
