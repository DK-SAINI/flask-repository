from app.article import app2
from flask import jsonify


@app2.route('/api/article_call', methods=['POST'])
def call_auth_app():
    # Return a response
    return jsonify({'message': 'Article App running.'}), 200
