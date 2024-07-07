from flask import Blueprint, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL
from flask import current_app


mysql = MySQL()
def loginauth(password,email,user_type):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM login WHERE email = %s AND password = %s AND user_type = %s", (email, password, user_type))
    result = cur.fetchone()
    if result:
        return True
    else:
        return False
    mysql.connection.commit()
    cur.close()

def get_username(password,email,user_type):
    cur = mysql.connection.cursor()
    cur.execute("SELECT username FROM login WHERE password = %s AND user_type = %s AND email = %s",(password, user_type, email))
    result = cur.fetchone()
    username = result[0]
    cur.close()
    return username

def get_id(password,email,user_type):
    cur = mysql.connection.cursor()
    cur.execute("SELECT id FROM login WHERE password = %s AND user_type = %s AND email = %s",(password, user_type, email))
    result = cur.fetchone()
    username = result[0]
    cur.close()
    return username