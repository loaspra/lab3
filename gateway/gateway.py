from flask import Flask, request, jsonify
from jwt import encode, decode, InvalidTokenError # una librería para manejar tokens JWT

import requests # una librería para hacer peticiones HTTP

app = Flask(__name__)

# Las direcciones de los microservicios (aquí se podrían usar variables de entorno o un archivo de configuración)
LYRICS_SERVICE_URL = "http://localhost:5000/obtener-letra"
AUTH_SERVICE_URL = "http://localhost:5001/verify"

@app.route("/artist-lyrics")
def artist_lyrics():
    token = request.headers.get("Authorization") # obtener el token del header de la petición
    if not token:
        # Devolver un mensaje de error si no hay token
        return jsonify({"error": "Missing token"}), 401
    response = requests.get(AUTH_SERVICE_URL, params={"token": token})

    if response.status_code == 200:
        # Input
        artist = request.args.get("artist")
        # Redirigir la petición al microservicio de letras
        response = requests.get(LYRICS_SERVICE_URL, params={"artist": artist})
        return jsonify(response.json())
    else:
        # Si el token es inválido, devolver un mensaje de error
        return jsonify({"error": "Invalid token"}), 401


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
