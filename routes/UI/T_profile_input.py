from flask import Blueprint, render_template, request, redirect, url_for, flash, session
import mysql.connector

T_profile_input_bp = Blueprint('T_profile_input_bp', __name__)

# データベース接続の設定
db_config = {
    'user': 'team08',
    'password': 'pass08',
    'host': 'localhost',
    'database': 'MATCHINGAPP'
}

@T_profile_input_bp.route('/profile', methods=['GET', 'POST'])
def T_profile_input():
    if request.method == 'POST':
        name = request.form.get('name')
        gender = request.form.get('gender')
        university = request.form.get('university')
        affiliation = request.form.get('affiliation')
        exam_experience = request.form.getlist('exam_experience')
        deviation_value = request.form.get('deviation_value')
        club_activity = request.form.get('club_activity')
        middle_school_type = request.form.get('middle_school_type')
        teaching_style = request.form.get('teaching_style')
        introduction = request.form.get('introduction')

        # フォームデータの検証
        errors = {}
        if not university:
            errors['university'] = '大学名を入力してください。'
        if not affiliation:
            errors['affiliation'] = '所属を入力してください。'
        if not deviation_value:
            errors['deviation_value'] = '偏差値を入力してください。'
        if not teaching_style:
            errors['teaching_style'] = '授業スタイルを選択してください。'

        if errors:
            form_data = request.form.to_dict()
            return render_template('T_profile_input.html', form_data=form_data, errors=errors, username=session.get('username'))

        # データベースへの接続とデータの挿入・更新
        try:
            conn = mysql.connector.connect(**db_config)
            cursor = conn.cursor()

            # 新しいプロフィールを挿入
            cursor.execute("""
                INSERT INTO teacher_profiles (name, gender, university, affiliation, 
                                             middle_school_exam, public_high_school_exam, 
                                             private_high_school_exam, public_university_exam, 
                                             private_university_exam, deviation_value, 
                                             club_activity, middle_school_type, 
                                             teaching_style, introduction)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """, (
                name, gender, university, affiliation,
                'middle_school_exam' in exam_experience,
                'public_high_school_exam' in exam_experience,
                'private_high_school_exam' in exam_experience,
                'public_university_exam' in exam_experience,
                'private_university_exam' in exam_experience,
                deviation_value, club_activity, middle_school_type,
                teaching_style, introduction
            ))

            conn.commit()
            cursor.close()
            conn.close()

            flash('プロフィールが正常に保存されました。')
            return redirect(url_for('T_homeview.teacher_home'))

        except mysql.connector.Error as err:
            flash(f"エラー: {err}")
            return redirect(url_for('T_profile_input_bp.T_profile_input'))

    # GETリクエストの場合はフォームを表示
    return render_template('T_profile_input.html', username=session.get('username'), form_data={}, errors={})

@T_profile_input_bp.route('/teacher_home')
def teacher_home():
    return render_template('T_homeview.html', username=session.get('username'))
