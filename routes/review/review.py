# # MatchingApp/routes/review/review.py

# from flask import Blueprint, request, redirect, url_for, session, flash
# from flask_mysqldb import MySQL
# from MatchingApp.app import mysql

# review_bp = Blueprint('review', __name__)

# @review_bp.route('/submit_review', methods=['POST'])
# def submit_review():
#     if 'student_id' in session:
#         student_id = session['student_id']
#         teacher_id = request.form.get('teacher_id')
#         rating = request.form.get('rating')
#         review = request.form.get('review')

#         if not teacher_id or not rating:
#             flash("Please fill in all fields.")
#             return redirect(url_for('evaluate_bp.evaluate_teacher'))

#         cur = mysql.connection.cursor()
#         cur.execute("INSERT INTO match_histories (student_id, teacher_id, rating, review) VALUES (%s, %s, %s, %s)",
#                     (student_id, teacher_id, rating, review))
#         mysql.connection.commit()
#         cur.close()

#         flash("Review submitted successfully!")
#         return redirect(url_for('homeview_bp.homeview'))
#     else:
#         flash("You need to login first.")
#         return redirect(url_for('login_bp.login'))
