""" API Blueprint Application """

from flask import Blueprint, current_app
from flask_restplus import Api

api_bp = Blueprint('api_bp', __name__, url_prefix='/api')
api_rest = Api(api_bp)


@api_bp.after_request
def add_header(response):
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type,Authorization'
    return response


from .webhook import *
from .process import *
