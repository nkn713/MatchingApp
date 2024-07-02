from flask import Blueprint, render_template, redirect, url_for, session

T_attend_day_bp = Blueprint('T_attend_day_bp', __name__)

@T_attend_day_bp.route('/attend_day')
def attend_day():
<<<<<<< HEAD
    if 'username' not in session:
        return redirect(url_for('login.login'))
=======
    #if 'username' not in session:
    #    return redirect(url_for('login.login'))
>>>>>>> b51f2a9bc66494a62777f80fe89a198d7948be7c
    return render_template('T_attend_day.html', username=session.get('username'))
