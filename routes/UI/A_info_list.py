# routes/A_info_list.py

from flask import Blueprint, render_template, session, redirect, url_for

# ブループリントの作成
admin_bp = Blueprint('admin', __name__, template_folder='templates')

@admin_bp.route('/admin_home')
def admin_home():
    if 'username' not in session:
        return redirect(url_for('login.login'))
    return render_template('A_homeview.html', username=session.get('username'))

@admin_bp.route('/info_list')
def info_list():
    if 'username' not in session:
        return redirect(url_for('login.login'))
    # ここで生徒・講師情報一覧画面の処理を実装する
    # 仮に生徒・講師情報のリストを取得する例を示す
    students = [
        {'id': 1, 'name': 'John Doe', 'grade': 'A'},
        {'id': 2, 'name': 'Jane Smith', 'grade': 'B'},
    ]
    teachers = [
        {'id': 101, 'name': 'Mike Johnson', 'subject': 'Math'},
        {'id': 102, 'name': 'Emily Brown', 'subject': 'Science'},
    ]
    return render_template('A_info_list.html', students=students, teachers=teachers)

@admin_bp.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login.login'))

# 他のルートや機能を追加する場合はここに記述