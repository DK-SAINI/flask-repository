from app.authentication import app1
from flask import jsonify


@app1.route('/api/auth_call', methods=['POST'])
def call_auth_app():
    # Return a response
    return jsonify({'message': 'Authenticating App running.'}), 200
