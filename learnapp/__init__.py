from learnapp.config import Config
from flask import Flask

def create_app(config_class=Config):
    app: Flask = Flask(__name__)
    app.config.from_object(Config)
    
    # Importing Blueprint
    from learnapp.main.routes import main
    
    # Connecting Blueprints
    app.register_blueprint(main)

    return app
