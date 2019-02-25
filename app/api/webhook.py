"""
REST API Resource Routing
http://flask-restplus.readthedocs.io
"""

from flask import request
from flask_restplus import Resource

from .services import get_service
from .security import require_auth
from . import api_rest


@api_rest.route('/webhook')
class Webhook(Resource):
    """ Unsecure Resource Class: Inherit from Resource """
    """ Calls require_auth decorator on all requests """
    method_decorators = [require_auth]

    def post(self):
        json_payload = request.get_json()
        service = get_service(json_payload['queryResult']['intent']['displayName'])
        return service(json_payload), 200
