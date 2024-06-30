from flask import Blueprint, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL 
from flask import current_app
       
       
mysql = MySQL()
def RegisterToDatabase(password,email,user_type,username):
    #追加
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO login (password, email, user_type,username) VALUES (%s, %s, %s, %s)", (password, email, user_type,username))
    mysql.connection.commit()
    cur.close()
    #追加
    