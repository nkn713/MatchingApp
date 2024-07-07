# routes/A_info_list.py

from flask import Blueprint, render_template, session, redirect, url_for

# ブループリントの作成
A_info_list_bp = Blueprint('A_info_list', __name__,)

@A_info_list_bp.route('/A_homeview')
def admin_home():
    if 'username' not in session:
        return redirect(url_for('login.login'))
    return render_template('A_homeview.html', username=session.get('username'))

