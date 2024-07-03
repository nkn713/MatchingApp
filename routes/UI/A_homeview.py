from flask import Flask, render_template, redirect, url_for, request
from flask_mysqldb import MySQL
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user

A_homeview_bp = Blueprint('A_homeview', __name__)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/')
@login_required
def admin():
    return render_template('admin.html', username=current_user.username)

@app.route('/info')
@login_required
def A_info_list():
    cur = mysql.connection.cursor()
    cur.execute("SELECT id, name, grade, gender, affiliation, desired_datetime, desired_subject FROM students")
    students = cur.fetchall()
    cur.execute("SELECT id, name, grade, gender, affiliation, desired_datetime, teachable_subjects, review FROM teachers")
    teachers = cur.fetchall()
    cur.close()
    return render_template('A_info_list.html', students=students, teachers=teachers, username=current_user.username)

