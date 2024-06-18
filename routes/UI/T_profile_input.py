from flask import Flask, render_template, request, redirect, url_for
from logout import logout_bp

app = Flask(__name__)

# ログアウトブループリントの登録
app.register_blueprint(logout_bp)

@app.route('/teacher_home')
def teacher_home():
    return render_template('teacher_homeview.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/submit_profile', methods=['POST'])
def submit_profile():
    name = request.form['name']
    gender = request.form['gender']
    affiliation = request.form['affiliation']
    grade = request.form['grade']
    # データを処理するロジックをここに追加
    # 例: データベースに保存する、その他の操作を行うなど
    return redirect(url_for('teacher_home'))

if __name__ == "__main__":
    app.run(debug=True)