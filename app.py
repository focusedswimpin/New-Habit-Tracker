import os
from flask import Flask
from routes import pages
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

def create_app():
    app = Flask(__name__)
    app.config.from_envvar('FLASK_ENV', silent=True)
    
    client = MongoClient(os.environ.get("MONGODB_URI"))
    app.db = client.get_default_database()

    app.register_blueprint(pages)

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
