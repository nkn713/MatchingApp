# routes/profile/profile_service1.py
from routes.profile.database_operations1 import get_db

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
