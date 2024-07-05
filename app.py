from flask import Flask
from flask_mysqldb import MySQL

from routes.UI.login import login_bp  # 正しいパスを指定
from routes.UI.login import login_bp
from routes.UI.logout import logout_bp
from routes.UI.S_homeview import S_homeview_bp
from routes.UI.S_evaluate_teacher import evaluate_bp
from routes.UI.register import register_bp
from routes.UI.S_select_teacher import S_select_teacher_bp
from routes.UI.S_attend_day import attend_day_bp
from routes.UI.S_take_subject import take_subject_bp
from routes.UI.T_homeview import T_homeview_bp
from routes.UI.T_take_attend import T_take_attend_bp
from routes.UI.T_take_subject import T_take_subject_bp
from routes.UI.A_homeview import A_homeview_bp
from routes.UI.A_info_list import A_info_list_bp
from routes.UI.A_matching_status import A_matching_status_bp
from routes.UI.S_profile_input import S_profile_input_bp
from routes.UI.T_profile_input import T_profile_input_bp
#from routes.review.review import review_bp
from routes.UI.S_take_attend import S_take_attend_bp


app = Flask(__name__)
app.secret_key = 'your_secret_key'

app.register_blueprint(login_bp, url_prefix='/')
app.register_blueprint(logout_bp, url_prefix='/')
app.register_blueprint(S_homeview_bp, url_prefix='/home')
app.register_blueprint(evaluate_bp, url_prefix='/evaluate')
app.register_blueprint(register_bp, url_prefix='/register')
app.register_blueprint(take_subject_bp, url_prefix='/take_subject')
app.register_blueprint(T_homeview_bp, url_prefix='/T_homeview')
app.register_blueprint(T_take_subject_bp, url_prefix='/take_subject')
app.register_blueprint(A_homeview_bp, url_prefix='/A_homeview')
app.register_blueprint(A_info_list_bp, url_prefix='/A_info_list')
app.register_blueprint(A_matching_status_bp, url_prefix='/matching_status')
#
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'team08'  # データベースのユーザ名
app.config['MYSQL_PASSWORD'] = 'pass08'  # データベースのパスワード
app.config['MYSQL_DB'] = 'MatchingApp'  # 使用するデータベース名
mysql = MySQL(app)
#

app.register_blueprint(S_select_teacher_bp, url_prefix='/S_select_teacher')
app.register_blueprint(S_profile_input_bp, url_prefix='/S_profile_input')
app.register_blueprint(T_profile_input_bp, url_prefix='/T_profile_input')
#app.register_blueprint(review_bp, url_prefix='/review')
app.register_blueprint(T_take_attend_bp, url_prefix='/T_take_attend')
app.register_blueprint(S_take_attend_bp, url_prefix='/S_take_attend')
if __name__ == '__main__':
    app.run(debug=True)
