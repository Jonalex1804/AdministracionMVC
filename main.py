from app import create_app, db
import os
from flask import redirect, url_for
from flask_login import login_required
from app.models import User
from werkzeug.security import generate_password_hash

app = create_app()

# Ruta raíz para mostrar mensaje básico
@app.route("/")
def home():
    return "Servidor Flask activo. Visita <a href='/login'>/login</a> para acceder."

# Ruta protegida
@app.route("/dashboard")
@login_required
def dashboard():
    return "Bienvenido al sistema, estás logueado correctamente."

# Ruta temporal para crear el usuario
@app.route("/create-user")
def create_user():
    username = "admin2003"
    password = "admin"

    if User.query.filter_by(username=username).first():
        return "El usuario ya existe."
    else:
        user = User(username=username, password=generate_password_hash(password))
        db.session.add(user)
        db.session.commit()
        return "Usuario creado exitosamente."

# Iniciar la app en Render
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
