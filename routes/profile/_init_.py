# routes/profile/__init__.py

from flask import Blueprint

profile_bp = Blueprint('profile', __name__, url_prefix='/profile')

from . import S_profile_input, T_profile_input, process_profile, view_profile, edit_profile
