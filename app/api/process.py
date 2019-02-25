"""
REST API Resource Routing
http://flask-restplus.readthedocs.io
"""

from flask import request
from flask_restplus import Resource

from .services import process_text
from .security import require_auth
from . import api_rest


@api_rest.route('/process')
class Process(Resource):
    method_decorators = [require_auth]

    def post(self):
        json_payload = request.get_json()
        response = process_text(json_payload['text'])
        return response, 200
