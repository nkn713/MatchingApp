from routes.profile.database_operations1 import get_db
import traceback

def process_student_profile(email, name, gender, preferred_gender, purpose, target_school_level, club_activity, school_type):
    print(f'Processing profile for {email}')
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
                        school_type = COALESCE(%s, school_type)
                    WHERE email = %s
                """
                params = (
                    name, gender, preferred_gender, purpose, target_school_level, 
                    club_activity, school_type, email
                )
            else:
                # レコードが存在しない場合、新規挿入
                sql = """
                    INSERT INTO student_profiles 
                    (email, name, gender, preferred_gender, purpose, target_school_level, club_activity, school_type) 
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                """
                params = (
                    email, name, gender, preferred_gender, purpose, target_school_level,
                    club_activity, school_type
                )

            print(f"SQL: {sql}")
            print(f"Params: {params}")
            cursor.execute(sql, params)
            db.commit()
            print('Profile saved to database')
    except Exception as e:
        print(f'Error saving profile: {e}')
        traceback.print_exc()
        raise e


def process_teacher_profile(email, name, gender, university, department, exam_experience, deviation_value, club_activity, middle_school_type, teaching_style, introduction, password):
    print(f'Processing profile for {email}')
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

            print(f"SQL: {sql}")
            print(f"Params: {params}")
            cursor.execute(sql, params)
            db.commit()
            print('Profile saved to database')
    except Exception as e:
        print(f'Error saving profile: {e}')
        traceback.print_exc()
        raise e
    