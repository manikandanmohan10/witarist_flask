from flask import request, Response, jsonify
from flask.views import MethodView

class TestView(MethodView):
    def post(self):
        return Response('From POST')

    def get(self):
        return Response('From GET')

    def put(self):
        return Response('From PUT')
    
    def delete(self):
        return Response('From DELETE')
    
    def patch(self):
        return Response('From PATCH')