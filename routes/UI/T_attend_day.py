from flask import Blueprint, render_template, redirect, url_for, session

T_attend_day_bp = Blueprint('T_attend_day_bp', __name__)

@T_attend_day_bp.route('/attend_day')
def attend_day():
    #if 'username' not in session:
    #    return redirect(url_for('login.login'))
    return render_template('T_attend_day.html', username=session.get('username'))
