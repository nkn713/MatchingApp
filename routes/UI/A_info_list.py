# from flask import Flask, render_template, session, redirect, url_for
# import mysql.connector

# app = Flask(__name__)
# app.secret_key = 'your_secret_key'

# def get_db_connection():
#     connection = mysql.connector.connect(
#         host='localhost',
#         user='team08',
#         password='pass08',
#         database='MatchingApp'
#     )
#     return connection

# @app.route('/admin_home')
# def admin_home():
#     if 'username' not in session:
#         return redirect(url_for('login'))
#     return render_template('A_homeview.html', username=session.get('username'))

# @app.route('/info_list')
# def info_list():
#     if 'username' not in session:
#         return redirect(url_for('login'))

#     connection = get_db_connection()
#     cursor = connection.cursor(dictionary=True)

#     cursor.execute('SELECT * FROM student_profiles')
#     students = cursor.fetchall()

#     cursor.execute('SELECT * FROM teacher_profiles')
#     teachers = cursor.fetchall()

#     cursor.close()
#     connection.close()

#     return render_template('A_info_list.html', students=students, teachers=teachers)

# @app.route('/logout')
# def logout():
#     session.pop('username', None)
#     return redirect(url_for('login'))

# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     # ログイン処理をここに実装
#     pass

# if __name__ == '__main__':
#     app.run(debug=True)
