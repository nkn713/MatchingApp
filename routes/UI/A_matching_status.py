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
            # 対象の行を見つけて、TrueをFalseに切り替える（この例では単純に反転する）
            for row in table_data:
                if row[0] == match_id:
                    row[3] = not row[3]  # TrueをFalseに、FalseをTrueに反転する
                    update_status_in_database(match_id)

        # 更新後、再度indexページにリダイレクトする
        return redirect(url_for('A_matching_status.html'))

