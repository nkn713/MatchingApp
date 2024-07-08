from flask import Blueprint, render_template, request, redirect, url_for, session
from routes.get_info.get_some_id import get_profile_id

T_matchinfo_bp = Blueprint('T_matchinfo',__name__)

@T_matchinfo_bp.route('/matchinfo')
def matchinfo():
    username = session.get('username')
    teacher_id = get_profile_id(session.get('id'))
    #get_match_info関数を作成して、match_infoをS_matchinfo.htmlへ渡す
    #match_info = get_match_info(student_id)
    return render_template('T_matchinfo.html', username=username)

