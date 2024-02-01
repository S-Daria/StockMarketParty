from flask import Flask
from .database import db  # Import db
from .manage_inputs import register_commands

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    db.init_app(app)

    # Import blueprints after db to avoid circular imports
    from .routes.guest_routes import guest_bp
    from .routes.drink_routes import drink_bp
    from .routes.activity_routes import activity_bp

    app.register_blueprint(guest_bp)
    app.register_blueprint(drink_bp)
    app.register_blueprint(activity_bp)

    register_commands(app, db)

    return app
