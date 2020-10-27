from flask import Blueprint

bp = Blueprint('main', __name__, url_prefix='/')

@bp.route('/hello')
def hello_kang():
    return 'Hello, Kang!'

@bp.route('/')
def index():
    return 'Kang index'