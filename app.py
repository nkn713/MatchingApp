from flask import Flask
from routes.UI.login import login_bp
from routes.UI.logout import logout_bp
from routes.UI.S_homeview import homeview_bp
from routes.UI.S_evaluate_teacher import evaluate_bp
from routes.UI.register import register_bp
from routes.UI.S_select_teacher import S_select_teacher_bp
from routes.UI.S_attend_day import attend_day_bp
from routes.UI.S_take_subject import take_subject_bp
from routes.UI.T_homeview import T_homeview_bp
from routes.UI.T_attend_day import T_attend_day_bp
from routes.UI.T_take_subject import T_take_subject_bp
<<<<<<< HEAD
from routes.UI.A_info_list import admin_bp
from routes.UI.S_profile_input import S_profile_input_bp
from routes.UI.T_profile_input import T_profile_input_bp
=======
# from routes.UI.A_info_list import admin_bp
#
>>>>>>> 365c53a5f73048adebc4e9dde8973ba8c2992b46
from flask_mysqldb import MySQL

app = Flask(__name__)
app.secret_key = 'your_secret_key'

#
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'team08'  # データベースのユーザ名
app.config['MYSQL_PASSWORD'] = 'pass08'  # データベースのパスワード
app.config['MYSQL_DB'] = 'MatchingApp'  # 使用するデータベース名
mysql = MySQL(app)
#

app.register_blueprint(login_bp, url_prefix='/')
app.register_blueprint(logout_bp, url_prefix='/')
app.register_blueprint(homeview_bp, url_prefix='/home')
app.register_blueprint(evaluate_bp, url_prefix='/evaluate')
app.register_blueprint(register_bp, url_prefix='/register')
app.register_blueprint(S_select_teacher_bp, url_prefix='/S_select_teacher')
app.register_blueprint(attend_day_bp, url_prefix='/attend_day')
app.register_blueprint(take_subject_bp, url_prefix='/take_subject')
app.register_blueprint(T_homeview_bp, url_prefix='/T_homeview')
app.register_blueprint(T_attend_day_bp, url_prefix='/attend_day')
app.register_blueprint(T_take_subject_bp, url_prefix='/take_subject')
<<<<<<< HEAD
app.register_blueprint(admin_bp, url_prefix='/admin')
app.register_blueprint(S_profile_input_bp, url_prefix='/S_profile_input')
app.register_blueprint(T_profile_input_bp, url_prefix='/T_profile_input')
=======
# app.register_blueprint(admin_bp, url_prefix='/admin')
>>>>>>> 365c53a5f73048adebc4e9dde8973ba8c2992b46

if __name__ == '__main__':
    app.run(debug=True)
