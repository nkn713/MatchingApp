from flask import Blueprint, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL 
from flask import current_app
       
       
mysql = MySQL()
def RegisterToDatabase(password,email,user_type,username):
    #追加
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO login (password, email, user_type,username) VALUES (%s, %s, %s, %s)", (password, email, user_type,username))
    if user_type == 'student':
        cur.execute("INSERT INTO student_profiles (name, email,password) VALUES (%s, %s, %s)", (username, email,password))
    elif user_type == 'teacher':
        cur.execute("INSERT INTO teacher_profiles (name, email,password) VALUES (%s, %s, %s)", (username, email,password))
    mysql.connection.commit()
    cur.close()
    #追加
    