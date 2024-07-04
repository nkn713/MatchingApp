from flask import Blueprint, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL 
from flask import current_app

def all_student():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM  MatchInfo ")
    table_data = cur.fetchall()
    mysql.connection.commit()
    cur.close()
    # HTMLテンプレートにテーブルのデータを渡してレンダリング
    return render_template('', table_data=table_data)

