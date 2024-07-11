from routes.profile.database_operations1 import get_db
import traceback

def process_student_profile(email, name, gender, preferred_gender, purpose, target_school_level, club_activity, school_type):
    print(f'Processing profile for {email}')
    db = get_db()
    try:
        cursor = db.cursor()
        sql = """
            INSERT INTO student_profiles 
            (email, name, gender, preferred_gender, purpose, target_school_level, club_activity, school_type, password) 
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        cursor.execute(sql, (email, name, gender, preferred_gender, purpose, target_school_level, club_activity, school_type, ''))
        db.commit()
        print('Profile saved to database')
    except Exception as e:
        print(f'Error saving profile: {e}')
        raise e
    finally:
        cursor.close()



def process_teacher_profile(email, name, gender, exam_experience, deviation_value, club_activity, middle_school_type, teaching_style, introduction, password):
    print(f'Processing profile for {email}')
    db = get_db()
    try:
        cursor = db.cursor()
        sql = """
            INSERT INTO teacher_profiles 
            (email, name, gender, exam_experience, deviation_value, club_activities, middle_school_type, teaching_style, introduction, password) 
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        params = (
            email, name, gender, exam_experience,
            int(deviation_value), club_activity, middle_school_type,
            teaching_style, introduction, password
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
    finally:
        cursor.close()
