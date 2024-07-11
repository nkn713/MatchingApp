from routes.profile.database_operations2 import get_db

def process_teacher_profile(email, name, gender, university, affiliation, exam_experience, deviation_value, club_activity, middle_school_type, teaching_style, introduction):
    print(f'Processing profile for {email}')
    db = get_db()
    try:
        cursor = db.cursor()
        sql = """
            INSERT INTO teacher_profiles 
            (email, name, gender, university, affiliation, middle_school_exam, public_high_school_exam, private_high_school_exam, public_university_exam, private_university_exam, deviation_value, club_activity, middle_school_type, teaching_style, introduction) 
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        cursor.execute(sql, (
            email, name, gender, university, affiliation,
            'middle_school_exam' in exam_experience,
            'public_high_school_exam' in exam_experience,
            'private_high_school_exam' in exam_experience,
            'public_university_exam' in exam_experience,
            'private_university_exam' in exam_experience,
            deviation_value, club_activity, middle_school_type,
            teaching_style, introduction
        ))
        db.commit()
        print('Profile saved to database')
    except Exception as e:
        print(f'Error saving profile: {e}')
        raise e
    finally:
        cursor.close()
