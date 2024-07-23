# routes/profile/database_operations1.py
from flask import current_app, g
from flask_mysqldb import MySQL

mysql = MySQL()

def init_app(app):
    mysql.init_app(app)

    @app.teardown_appcontext
    def close_db(error):
        if hasattr(g, 'db'):
            g.db.close()

def get_db():
    if 'db' not in g:
        g.db = mysql.connection
    return g.db
