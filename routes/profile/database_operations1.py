# routes/profile/database_operations1.py
from flask import current_app, g
from flask_mysqldb import MySQL

mysql = MySQL()

def init_app(app):
    mysql.init_app(app)

def get_db():
    if 'db' not in g:
        g.db = mysql.connection
    return g.db
