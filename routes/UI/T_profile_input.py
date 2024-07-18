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
        return redirect(url_for('login.login'))

    if request.method == 'POST':
        gender = request.form.get('gender')
        university = request.form.get('university')
        department = request.form.get('department')  # 新しいフィールド
        exam_experience = request.form.getlist('exam_experience')  # getlistで複数のチェックボックスの値を取得
        deviation_value = request.form.get('deviation_value')
        club_activity = request.form.get('club_activity')
        middle_school_type = request.form.get('middle_school_type')
        teaching_style = request.form.get('teaching_style')
        introduction = request.form.get('introduction')

        # デバッグ: フォームデータの出力
        print(f"gender: {gender}, university: {university}, department: {department}, "
              f"exam_experience: {exam_experience}, deviation_value: {deviation_value}, club_activity: {club_activity}, "
              f"middle_school_type: {middle_school_type}, teaching_style: {teaching_style}, introduction: {introduction}")

        # フォームデータの検証
        errors = {}
        if not university:
            errors['university'] = '大学名を入力してください。'
        if not department:
            errors['department'] = '学科を入力してください。'
        if not deviation_value:
            errors['deviation_value'] = '偏差値を入力してください。'
        if not teaching_style:
            errors['teaching_style'] = '授業スタイルを選択してください。'

        if errors:
            form_data = request.form.to_dict(flat=False)
            form_data['exam_experience'] = exam_experience  # リストを含める
            return render_template('T_profile_input.html', form_data=form_data, errors=errors, username=session.get('username'))

        # exam_experience がリストであることを確認
        if not isinstance(exam_experience, list):
            exam_experience = []

        try:
            # exam_experience が空なら None を設定
            exam_experience_str = ','.join(exam_experience) if exam_experience else None

            # デバッグ: process_teacher_profileに渡されるデータの出力
            print(f"process_teacher_profile called with: email={email}, name={name}, gender={gender}, university={university}, "
                  f"department={department}, exam_experience={exam_experience_str}, deviation_value={deviation_value}, "
                  f"club_activity={club_activity}, middle_school_type={middle_school_type}, teaching_style={teaching_style}, "
                  f"introduction={introduction}, password={password}")

            process_teacher_profile(
                email, name, gender, university, department, exam_experience_str, deviation_value, club_activity,
                middle_school_type, teaching_style, introduction, password
            )
            flash('プロフィールが正常に保存されました。', 'success')
            return redirect(url_for('T_profile_input_bp.teacher_home'))
        except ValidationError as error:
            message, field_name = handle_error(error)
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
