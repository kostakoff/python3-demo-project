"""Flask application factory and endpoints"""
import os
from flask import Flask, send_from_directory
from .version import __version__

def create_app():
    static_folder = os.path.join(os.path.dirname(__file__), "static")
    app = Flask(__name__, static_folder=static_folder)

    @app.route("/version")
    def version():
        return {"version": __version__}

    @app.route("/static/<path:filename>")
    def static_files(filename):
        return send_from_directory(static_folder, filename)

    @app.route("/")
    def index():
        return {"message": "Hello from demo_flask"}

    return app

if __name__ == "__main__":
    # For ad‑hoc launches — use CLI for production
    app = create_app()
    app.run(host="0.0.0.0", port=5000)
