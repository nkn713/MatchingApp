# reviewボタンを押されたら、1-5の間で選択できるボタンとコメントを書き込めるテキストボックスを表示し、更新ボタンを押されたらデータが挿入されるようにしてください

# routes/review/review.py
from flask import Blueprint

review_bp = Blueprint('review_bp', __name__)

@review_bp.route('/some_route')
def some_route():
    return "This is a route in the review blueprint"

