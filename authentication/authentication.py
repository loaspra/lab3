from flask import Flask, request, jsonify
from jwt import encode, decode, InvalidTokenError

app = Flask(__name__)

SECRET_KEY = "some_secret_key" # una clave secreta para cifrar y descifrar los tokens

@app.route("/login")
def login():
    username = request.args.get("username") # obtener el nombre de usuario como parámetro
    password = request.args.get("password") # obtener la contraseña como parámetro

    # Credenciales de ejemplo
    if username == "batman" and password == "clave123":
        # Generar el token con el nombre de usuario y una fecha de expiración
        token = encode({"username": username, "exp": 3600}, SECRET_KEY, algorithm="HS256")

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


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

