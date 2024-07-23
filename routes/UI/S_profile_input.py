from flask import Blueprint, render_template, request, redirect, url_for, flash, session, current_app
from routes.profile.profile_service1 import process_student_profile
from routes.profile.error_handling import ValidationError, handle_error
import traceback

S_profile_input_bp = Blueprint('S_profile_input_bp', __name__)

@S_profile_input_bp.route('/student_home')
def student_home():
    username = session.get('username')
    if not username:
        flash('セッションにユーザー名がありません。再度ログインしてください。', 'error')
        return redirect(url_for('login.login'))
    return render_template('S_homeview.html', username=username)

@S_profile_input_bp.route('/profile', methods=['GET', 'POST'])
def profile():
    email = session.get('email')
    username = session.get('username')  # セッションから名前を取得
    password = session.get('password')  # セッションからパスワードを取得

    if not email:
        flash('セッションにメールアドレスがありません。再度ログインしてください。', 'error')
        return redirect(url_for('login.login'))

    if request.method == 'POST':
        gender = request.form.get('gender')
        preferred_gender = request.form.get('preference')
        purpose = request.form.get('learning_purpose')
        target_school_level = request.form.get('desired_school_level')
        club_activity = request.form.get('club_activity')
        school_type = request.form.get('school_type')

        # デバッグ: フォームデータの出力
        current_app.logger.debug(f"gender: {gender}, preferred_gender: {preferred_gender}, purpose: {purpose}, "
                                 f"target_school_level: {target_school_level}, club_activity: {club_activity}, "
                                 f"school_type: {school_type}")

        # フォームデータの検証
        errors = {}
        if not purpose:
            errors['purpose'] = '目的を入力してください。'
        if not target_school_level:
            errors['target_school_level'] = '志望校のレベル（偏差値）を入力してください。'

        if errors:
            form_data = request.form.to_dict(flat=False)
            return render_template('S_profile_input.html', form_data=form_data, errors=errors, username=username)

        try:
            process_student_profile(
                email, username, gender, preferred_gender, purpose, target_school_level, club_activity, school_type, password
            )
            flash('プロフィールが正常に保存されました。', 'success')
            return redirect(url_for('S_profile_input_bp.student_home'))
        except ValidationError as error:
            message, field_name = handle_error(error)
            errors[field_name] = message
            return render_template('S_profile_input.html', username=username, form_data=request.form.to_dict(), errors=errors)
        except Exception as e:
            current_app.logger.error(f'予期しないエラーが発生しました: {e}')  # ログにエラーを記録
            current_app.logger.error(traceback.format_exc())
            flash(f'予期しないエラーが発生しました: {e}', 'error')
            return render_template('S_profile_input.html', username=username, form_data=request.form.to_dict(), errors={})

    # GETリクエストの場合はフォームを表示
    return render_template('S_profile_input.html', username=username, form_data={}, errors={})
