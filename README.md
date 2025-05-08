# Flask CRUD con DEUDAS

Este es un proyecto de ejemplo de CRUD de productos usando Flask con autenticación básica, protegido por login y estructura MVC.

## 🔧 Tecnologías usadas

- Python 3
- Flask
- Flask-WTF
- Flask-Login
- Flask-SQLAlchemy
- MySQL

## 🚀 Instrucciones para correr el proyecto


1. Instala las dependencias:

```
pip install -r requirements.txt
```

2. Crea la base de datos en MySQL:

```
CREATE DATABASE crud_deudas CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

3. Crea un usuario de prueba:

```
python create_user.py
```

4. Ejecuta la aplicación:

```
python main.py
```

### 👤 Usuario demo:

```
usuario: admin
contraseña: admin123
```