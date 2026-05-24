"""Flask API server integration."""

from flask import Flask, jsonify, request
from config import FLASK_HOST, FLASK_PORT


def create_app():
    """Create and configure Flask app."""
    app = Flask(__name__)
    
    @app.route('/health', methods=['GET'])
    def health():
        """Health check endpoint."""
        return jsonify({'status': 'healthy'}), 200
    
    @app.route('/webhook', methods=['POST'])
    def webhook():
        """Webhook endpoint for Telegram updates."""
        data = request.get_json()
        return jsonify({'ok': True}), 200
    
    return app


def run_server(app):
    """Run the Flask server."""
    app.run(host=FLASK_HOST, port=FLASK_PORT, debug=False)