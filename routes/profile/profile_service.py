from routes.profile.database_operations import save_student_profile, save_teacher_profile
from routes.profile.error_handling import ValidationError

def validate_student_profile(name, gender, affiliation, grade):
    """Validate student profile data."""
    if not isinstance(name, str) or len(name.encode('utf-8')) > 255:
        raise ValidationError('名前は255バイト以内の文字列である必要があります。', 'name')

    if not isinstance(affiliation, str) or len(affiliation.encode('utf-8')) > 255:
        raise ValidationError('所属は255バイト以内の文字列である必要があります。', 'affiliation')

    try:
        grade = int(grade)
        if grade < 1 or grade > 9:
            raise ValueError
    except ValueError:
        raise ValidationError('学年は1から9の間の整数である必要があります。', 'grade')

def process_student_profile(email, name, gender, affiliation, grade):
    """Process and save student profile data."""
    validate_student_profile(name, gender, affiliation, grade)
    save_student_profile(email, name, gender, affiliation, grade)

def validate_teacher_profile(name, gender, affiliation, university):
    """Validate student profile data."""
    if not isinstance(name, str) or len(name.encode('utf-8')) > 255:
        raise ValidationError('名前は255バイト以内の文字列である必要があります。', 'name')

    if not isinstance(affiliation, str) or len(affiliation.encode('utf-8')) > 255:
        raise ValidationError('所属は255バイト以内の文字列である必要があります。', 'affiliation')
    
    if not isinstance(university, str) or len(university.encode('utf-8')) > 255:
        raise ValidationError('大学名は255バイト以内の文字列である必要があります。', 'affiliation')

def process_teacher_profile(email, name, gender, affiliation, grade):
    """Process and save student profile data."""
    validate_teacher_profile(name, gender, affiliation, grade)
    save_teacher_profile(email, name, gender, affiliation, grade)
