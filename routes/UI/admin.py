# routes/admin.py

from flask import Blueprint, render_template, session, redirect, url_for

# ブループリントの作成
admin_bp = Blueprint('admin', __name__, template_folder='templates')

@admin_bp.route('/admin_home')
def admin_home():
    if 'username' not in session:
        return redirect(url_for('login.login'))
    return render_template('A_homeview.html', username=session.get('username'))

@admin_bp.route('/info')
def info():
    if 'username' not in session:
        return redirect(url_for('login.login'))
    return render_template('A_info_list.html')

@admin_bp.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login.login'))

# 他のルートや機能を追加する場合はここに記述
