from app import create_app
import os
from flask import redirect, url_for
from flask_login import login_required

app = create_app()

@app.route("/")
def home():
    return "Servidor Flask activo. Visita <a href='/login'>/login</a> para acceder."

@app.route("/dashboard")
@login_required
def dashboard():
    return "Bienvenido al sistema, estás logueado correctamente."

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))  
    app.run(host="0.0.0.0", port=port)
