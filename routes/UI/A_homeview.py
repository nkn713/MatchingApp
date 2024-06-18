from flask import Flask, render_template, redirect, url_for, request
from flask_mysqldb import MySQL
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user

app = Flask(__name__)

# MySQL configuration
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'your_password'
app.config['MYSQL_DB'] = 'your_database_name'
app.config['SECRET_KEY'] = 'your_secret_key'

mysql = MySQL(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

class User(UserMixin):
    def __init__(self, id, username):
        self.id = id
        self.username = username

@login_manager.user_loader
def load_user(user_id):
    cur = mysql.connection.cursor()
    cur.execute("SELECT id, username FROM users WHERE id = %s", (user_id,))
    user = cur.fetchone()
    cur.close()
    if user:
        return User(id=user[0], username=user[1])
    return None

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        cur = mysql.connection.cursor()
        cur.execute("SELECT id, username, password FROM users WHERE username = %s", (username,))
        user = cur.fetchone()
        cur.close()
        if user and user[2] == password:  # Password check should be hashed in real applications
            login_user(User(id=user[0], username=user[1]))
            return redirect(url_for('admin'))
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/')
@login_required
def admin():
    return render_template('admin.html', username=current_user.username)

@app.route('/info')
@login_required
def info():
    cur = mysql.connection.cursor()
    cur.execute("SELECT id, name, grade, gender, affiliation, desired_datetime, desired_subject FROM students")
    students = cur.fetchall()
    cur.execute("SELECT id, name, grade, gender, affiliation, desired_datetime, teachable_subjects, review FROM teachers")
    teachers = cur.fetchall()
    cur.close()
    return render_template('info.html', students=students, teachers=teachers, username=current_user.username)

if __name__ == '__main__':
    app.run(debug=True)
