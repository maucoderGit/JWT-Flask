from flask import Blueprint, jsonify, request

from function_jwt import validate_token, write_token

routes_auth = Blueprint('routes_auth', __name__)

@routes_auth.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    if data['username'] == 'maucoder':
        return write_token(data=request.get_json())
    else:
        response = jsonify({'message': 'User not found'})
        response.status_code = 404

        return response

@routes_auth.route('/verify/token')
def verify():
    token = (request.headers['Authorization'].split(' '))[1]

    return validate_token(token, output=True)