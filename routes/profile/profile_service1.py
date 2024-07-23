from routes.profile.database_operations1 import get_db
import traceback
from flask import current_app

def process_student_profile(email, name, gender, preferred_gender, purpose, target_school_level, club_activity, school_type, password):
    current_app.logger.debug(f'Processing profile for {email}')
    db = get_db()
    try:
        with db.cursor() as cursor:
            # レコードが存在するか確認
            cursor.execute("SELECT id FROM student_profiles WHERE email = %s", (email,))
            result = cursor.fetchone()

            if result:
                # レコードが存在する場合、更新
                sql = """
                    UPDATE student_profiles 
                    SET name = COALESCE(%s, name),
                        gender = COALESCE(%s, gender),
                        preferred_gender = COALESCE(%s, preferred_gender),
                        purpose = COALESCE(%s, purpose),
                        target_school_level = COALESCE(%s, target_school_level),
                        club_activity = COALESCE(%s, club_activity),
                        school_type = COALESCE(%s, school_type),
                        password = COALESCE(%s, password)
                    WHERE email = %s
                """
                params = (
                    name, gender, preferred_gender, purpose, target_school_level, 
                    club_activity, school_type, password, email
                )
            else:
                # レコードが存在しない場合、新規挿入
                sql = """
                    INSERT INTO student_profiles 
                    (email, name, gender, preferred_gender, purpose, target_school_level, club_activity, school_type, password) 
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
                """
                params = (
                    email, name, gender, preferred_gender, purpose, target_school_level,
                    club_activity, school_type, password
                )

            current_app.logger.debug(f"SQL: {sql}")
            current_app.logger.debug(f"Params: {params}")
            cursor.execute(sql, params)
            db.commit()
            current_app.logger.info('Profile saved to database')
    except Exception as e:
        current_app.logger.error(f'Error saving profile: {e}')
        current_app.logger.error(traceback.format_exc())
        raise e


def process_teacher_profile(email, name, gender, university, department, exam_experience, deviation_value, club_activity, middle_school_type, teaching_style, introduction, password):
    current_app.logger.debug(f'Processing profile for {email}')
    db = get_db()
    try:
        with db.cursor() as cursor:
            # レコードが存在するか確認
            cursor.execute("SELECT id FROM teacher_profiles WHERE email = %s", (email,))
            result = cursor.fetchone()

            if result:
                # レコードが存在する場合、更新
                sql = """
                    UPDATE teacher_profiles 
                    SET name = COALESCE(%s, name),
                        gender = COALESCE(%s, gender),
                        university = COALESCE(%s, university),
                        department = COALESCE(%s, department),
                        exam_experience = COALESCE(%s, exam_experience),
                        deviation_value = COALESCE(%s, deviation_value),
                        club_activities = COALESCE(%s, club_activities),
                        middle_school_type = COALESCE(%s, middle_school_type),
                        teaching_style = COALESCE(%s, teaching_style),
                        introduction = COALESCE(%s, introduction),
                        password = COALESCE(%s, password)
                    WHERE email = %s
                """
                params = (
                    name, gender, university, department, exam_experience, deviation_value, 
                    club_activity, middle_school_type, teaching_style, introduction, password, email
                )
            else:
                # レコードが存在しない場合、新規挿入
                sql = """
                    INSERT INTO teacher_profiles 
                    (email, name, gender, university, department, exam_experience, deviation_value, club_activity, middle_school_type, teaching_style, introduction, password) 
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                """
                params = (
                    email, name, gender, university, department, exam_experience, deviation_value,
                    club_activity, middle_school_type, teaching_style, introduction, password
                )

            current_app.logger.debug(f"SQL: {sql}")
            current_app.logger.debug(f"Params: {params}")
            cursor.execute(sql, params)
            db.commit()
            current_app.logger.info('Profile saved to database')
    except Exception as e:
        current_app.logger.error(f'Error saving profile: {e}')
        current_app.logger.error(traceback.format_exc())
        raise e
