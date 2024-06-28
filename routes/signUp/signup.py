from flask import Blueprint, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL 
from flask import current_app
       
       
    mysql = MySQL()
    def RegisterToDatabase(password,email,user_type):
        #追加
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO login (password, email, user_type) VALUES (%s, %s, %s)", (password, email, user_type))
        mysql.connection.commit()
        cur.close()
        #追加