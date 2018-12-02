from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from feature_req.config import Config


db = SQLAlchemy()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class) 
    db.init_app(app)

    from .routes import feature_req
    app.register_blueprint(feature_req)
    
    return app
   







