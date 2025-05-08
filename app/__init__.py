from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()
login_manager = LoginManager()
login_manager.login_view = 'auth.login'

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'f4c0f510ea3e495f6cda38511aae3491'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/flask_crud_deudas'

    db.init_app(app)
    login_manager.init_app(app)

    from .models import User

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    from .routes.auth_routes import auth_bp
    from .routes.debt_routes import debt_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(debt_bp)

    with app.app_context():
        db.create_all()

    return app