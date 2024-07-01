from flask import Blueprint, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL 
from flask import current_app
       
       
mysql = MySQL()
def RegisterToDatabase(password,email,user_type,username):
    #追加
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO login (password, email, user_type,username) VALUES (%s, %s, %s, %s)", (password, email, user_type,username))
    cur.execute("INSERT INTO student_profiles (name, email,passward) VALUES (%s, %s, %s)", (username, email,passward))
    cur.execute("INSERT INTO teacher_profiles (name, email,passward) VALUES (%s, %s, %s)", (username, email,passward))
    mysql.connection.commit()
    cur.close()
    #追加
    