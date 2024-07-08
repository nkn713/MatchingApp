from flask import Flask,Blueprint, render_template, redirect, url_for, request
from flask_mysqldb import MySQL
#from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user

A_homeview_bp = Blueprint('A_homeview', __name__)

mysql = MySQL()
@A_homeview_bp.route('/A_info_list')
def A_info_list():
    cur = mysql.connection.cursor()
    cur.execute("SELECT id, name, email, password, gender FROM student_profiles")
    students = cur.fetchall()
    cur.execute("SELECT id, name, email, password, gender FROM teacher_profiles")
    teachers = cur.fetchall()
    cur.close()
    return render_template('A_info_list.html', students=students, teachers=teachers)

@A_homeview_bp.route('/A_matching_status')
def A_matching_status():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM  MatchInfo ")
    table_data = cur.fetchall()
    cur.close()
    return render_template('A_matching_status.html', table_data=table_data)
