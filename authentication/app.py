from flask import Flask, request, jsonify
from jwt import encode, decode, InvalidTokenError # una librería para manejar tokens JWT

app = Flask(__name__)

SECRET_KEY = "some_secret_key" # una clave secreta para cifrar y descifrar los tokens

@app.route("/login")
def login():
    username = request.args.get("username") # obtener el nombre de usuario como parámetro
    password = request.args.get("password") # obtener la contraseña como parámetro
    # Validar las credenciales del usuario (aquí se podría usar una base de datos o un archivo)
    if username == "batman" and password == "clave123":
        # Generar el token con el nombre de usuario y una fecha de expiración
        token = encode({"username": username, "exp": 3600}, SECRET_KEY, algorithm="HS256")
        # Devolver el token como respuesta en formato JSON
        return jsonify({"token": token})
    else:
        # Devolver un mensaje de error si las credenciales son inválidas
        return jsonify({"error": "Invalid credentials"}), 401

@app.route("/verify")
def verify():
    token = request.args.get("token") # obtener el token como parámetro
    try:
        # Validar el token con la clave secreta y el algoritmo usado
        payload = decode(token, SECRET_KEY, algorithms=["HS256"])
        # Devolver el nombre de usuario como respuesta en formato JSON
        return jsonify({"username": payload["username"]})
    except InvalidTokenError:
        # Devolver un mensaje de error si el token es inválido o ha expirado
        return jsonify({"error": "Invalid token"}), 401
    

"""
Probar:
# Obtener un token con las credenciales válidas
curl http://localhost:5002/login?username=user&password=pass

# Hacer una petición al API Gateway con el token obtenido
curl http://localhost:5003/artist-lyrics?artist=ABBA -H "Authorization: <token>"

"""