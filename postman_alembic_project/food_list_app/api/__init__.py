# api/__init__.py
# this file is an extension of the code in app.py.
# it runs automatically when app.py is run.
from flask import Flask
from api.models import Base
from api.db import engine, SessionLocal
from api.routes import v1_bp

def create_app():
    # create a Flask instance.
    app = Flask(__name__)

    # psycopg2 enabled apis require engine and sessionlocal objects to manage connection
    # (initalised in db.py)

    # these objects are passed to each route in routes.py for real-time db commits.
    # v1_bp is the almalgation of the psycopg2 enabled routes.

    Base.metadata.create_all(bind=engine)  # Create tables if not exist

    # Register Blueprint with dependency injection for session
    app.register_blueprint(v1_bp, url_prefix='/api/v1', provide={'db': SessionLocal})

    return app
