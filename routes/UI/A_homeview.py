from flask import Flask,Blueprint, render_template, redirect, url_for, request
from flask_mysqldb import MySQL
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user

A_homeview_bp = Blueprint('A_homeview', __name__)

@A_homeview_bp.route('/A_info_list')
def A_info_list():
    cur = mysql.connection.cursor()
    cur.execute("SELECT id, name, grade, gender, affiliation, desired_datetime, desired_subject FROM students")
    students = cur.fetchall()
    cur.execute("SELECT id, name, grade, gender, affiliation, desired_datetime, teachable_subjects, review FROM teachers")
    teachers = cur.fetchall()
    cur.close()
    return render_template('A_info_list.html', students=students, teachers=teachers, username=current_user.username)

