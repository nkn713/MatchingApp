from flask import Blueprint, render_template, request, redirect, url_for, session

S_homeview_bp = Blueprint('S_homeview', __name__)

@S_homeview_bp.route('/')
def index():
    return render_template('S_homeview.html', id = session.get('id'), username = session.get('username'))

@S_homeview_bp.route('/S_profile_input')
def S_profile_input():
    return render_template('S_profile_input.html' ,id = session.get('id'), username=session.get('username'), form_data={}, errors={})

@S_homeview_bp.route('/S_evaluate_teacher')
def S_evaluate_teacher():
    return render_template('S_evaluate_teacher.html', id = session.get('id'), username = session.get('username'))

@S_homeview_bp.route('/S_take_attend')
def S_take_attend():
    return render_template('S_take_attend.html', id = session.get('id'), username = session.get('username'))
