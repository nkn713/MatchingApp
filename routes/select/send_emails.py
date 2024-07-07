import mysql.connector
from flask_mail import Mail, Message
from flask import Flask

app = Flask(__name__)

# Flask-Mailの設定
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = 'al22099@gmail.com'
app.config['MAIL_PASSWORD'] = 'tsuoi_dayo1205'
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False

mail = Mail(app)

# データベース接続の設定
db_config = {
    'user': 'team08',
    'password': 'pass08',
    'host': 'localhost',
    'database': 'MATCHINGAPP'
}

def send_match_emails(match_id):
    # データベースに接続
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor(dictionary=True)
    
    # マッチ情報を取得
    cursor.execute("""
        SELECT mi.Student_id, mi.Teacher_id, sp.name AS student_name, sp.email AS student_email,
               tp.name AS teacher_name, tp.email AS teacher_email
        FROM MatchInfo mi
        JOIN student_profiles sp ON mi.Student_id = sp.id
        JOIN teacher_profiles tp ON mi.Teacher_id = tp.id
        WHERE mi.Match_id = %s
    """, (match_id,))
    
    match_info = cursor.fetchone()
    cursor.close()
    conn.close()

    if not match_info:
        print('マッチ情報が見つかりません')
        return

    # メールの内容を作成
    student_message = f"{match_info['teacher_name']}とマッチ完了しました。"
    teacher_message = f"{match_info['student_name']}とマッチ完了しました。"

    try:
        # 生徒にメールを送信
        student_email_msg = Message("マッチ完了通知", sender=app.config['MAIL_USERNAME'], recipients=[match_info['student_email']])
        student_email_msg.body = student_message
        with app.app_context():
            mail.send(student_email_msg)
        
        # 講師にメールを送信
        teacher_email_msg = Message("マッチ完了通知", sender=app.config['MAIL_USERNAME'], recipients=[match_info['teacher_email']])
        teacher_email_msg.body = teacher_message
        with app.app_context():
            mail.send(teacher_email_msg)

        print('メールが正常に送信されました')

    except Exception as e:
        print(f'エラー: {str(e)}')

def send_unmatching_email(match_id):
    # データベースに接続
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor(dictionary=True)
    
    # マッチ情報を取得
    cursor.execute("""
        SELECT mi.Student_id, mi.Teacher_id, sp.name AS student_name, sp.email AS student_email,
               tp.name AS teacher_name, tp.email AS teacher_email
        FROM MatchInfo mi
        JOIN student_profiles sp ON mi.Student_id = sp.id
        JOIN teacher_profiles tp ON mi.Teacher_id = tp.id
        WHERE mi.Match_id = %s
    """, (match_id,))
    
    match_info = cursor.fetchone()
    cursor.close()
    conn.close()

    if not match_info:
        print('マッチ情報が見つかりません')
        return

    # メールの内容を作成
    student_message = f"{match_info['teacher_name']}とのマッチが解除されました。"
    teacher_message = f"{match_info['student_name']}とのマッチが解除されました。"

    try:
        # 生徒にメールを送信
        student_email_msg = Message("マッチ解除通知", sender=app.config['MAIL_USERNAME'], recipients=[match_info['student_email']])
        student_email_msg.body = student_message
        with app.app_context():
            mail.send(student_email_msg)
        
        # 講師にメールを送信
        teacher_email_msg = Message("マッチ解除通知", sender=app.config['MAIL_USERNAME'], recipients=[match_info['teacher_email']])
        teacher_email_msg.body = teacher_message
        with app.app_context():
            mail.send(teacher_email_msg)

        print('メールが正常に送信されました')

    except Exception as e:
        print(f'エラー: {str(e)}')

# 使用例
#send_match_emails(1)
# send_unmatching_email(1)
