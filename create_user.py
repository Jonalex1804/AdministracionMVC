from app import create_app, db
from app.models import User
from werkzeug.security import generate_password_hash

app = create_app()

with app.app_context():
    username = 'admin2003'
    password = 'admin'

    if User.query.filter_by(username=username).first():
        print("El usuario ya existe.")
    else:
        user = User(username=username, password=generate_password_hash(password))
        db.session.add(user)
        db.session.commit()
        print("Usuario creado exitosamente.")