from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from routes.profile.profile_service1 import process_teacher_profile
from routes.profile.error_handling import ValidationError, handle_error

T_profile_input_bp = Blueprint('T_profile_input_bp', __name__)

@T_profile_input_bp.route('/profile', methods=['GET', 'POST'])
def T_profile_input():
    email = session.get('email')
    name = session.get('username')  # セッションから名前を取得
    password = session.get('password')  # セッションからパスワードを取得
    if not email:
        flash('セッションにメールアドレスがありません。再度ログインしてください。', 'error')
        return redirect(url_for('register.login'))

    if request.method == 'POST':
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

        # exam_experience がリストであることを確認
        if not isinstance(exam_experience, list):
            exam_experience = []

        middle_school_exam = 'middle_school_exam' in exam_experience
        public_high_school_exam = 'public_high_school_exam' in exam_experience
        private_high_school_exam = 'private_high_school_exam' in exam_experience
        public_university_exam = 'public_university_exam' in exam_experience
        private_university_exam = 'private_university_exam' in exam_experience

        try:
            # exam_experience を文字列に変換
            exam_experience_str = ','.join(exam_experience)

            process_teacher_profile(
                email, name, gender, exam_experience_str, deviation_value, club_activity,
                middle_school_type, teaching_style, introduction, password
            )
            flash('プロフィールが正常に保存されました。', 'success')
            return redirect(url_for('T_profile_input_bp.teacher_home'))
        except ValidationError as error:
            message, category, field_name = handle_error(error)
            errors[field_name] = message
            return render_template('T_profile_input.html', username=session.get('username'), form_data=request.form.to_dict(), errors=errors)
        except Exception as e:
            flash(f'予期しないエラーが発生しました: {e}', 'error')
            return render_template('T_profile_input.html', username=session.get('username'), form_data=request.form.to_dict(), errors={})

    # GETリクエストの場合はフォームを表示
    return render_template('T_profile_input.html', username=session.get('username'), form_data={}, errors={})

@T_profile_input_bp.route('/teacher_home')
def teacher_home():
    return render_template('T_homeview.html', username=session.get('username'))
