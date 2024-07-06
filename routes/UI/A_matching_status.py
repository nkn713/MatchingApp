from flask import Blueprint, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL 
from flask import current_app

A_matching_status_bp = Blueprint('A_matching_status', __name__,)

mysql = MySQL()

def update_status_in_database(match_id):
    cur = mysql.connection.cursor()
    cur.execute("UPDATE MatchInfo SET match_status = 0 WHERE match_id = %s", (match_id,))
    mysql.connection.commit()
    cur.close()

@A_matching_status_bp.route('/toggle_status/<int:match_id>', methods=['POST'])
def toggle_status(match_id):
    if request.method == 'POST':
        action = request.form['action']
        if action == 'toggle':
            update_status_in_database(match_id)
            return redirect(url_for('A_matching_status.display_matching_status'))

@A_matching_status_bp.route('/matching_status', methods=['GET'])
def display_matching_status():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM MatchInfo")
    table_data = cur.fetchall()
    cur.close()
    return render_template('A_matching_status.html', table_data=table_data)

@A_matching_status_bp.route('/A_homeview')
def A_homeview():
     return render_template('A_homeview.html', username = session.get('username') ,id = session.get('id'))
