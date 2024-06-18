from flask import Flask
from routes.UI.login import login_bp  # 正しいパスを指定

app = Flask(__name__)
app.secret_key = 'your_secret_key'

app.register_blueprint(login_bp, url_prefix='/')


if __name__ == '__main__':
    app.run(debug=True)
