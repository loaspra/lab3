from flask import Flask, request, jsonify
from jwt import encode, decode, InvalidTokenError # una librería para manejar tokens JWT

import requests # una librería para hacer peticiones HTTP

app = Flask(__name__)

# Las direcciones de los microservicios (aquí se podrían usar variables de entorno o un archivo de configuración)
LYRICS_SERVICE_URL = "http://localhost:5000/obtener-letra"
AUTH_SERVICE_URL = "http://localhost:5003/verify"

@app.route("/artist-lyrics")
def artist_lyrics():
    token = request.headers.get("Authorization") # obtener el token del header de la petición
    if not token:
        # Devolver un mensaje de error si no hay token
        return jsonify({"error": "Missing token"}), 401
    # Verificar el token con el servicio de autenticación
    response = requests.get(AUTH_SERVICE_URL, params={"token": token})
    if response.status_code == 200:
        # Si el token es válido, obtener el nombre del artista como parámetro
        artist = request.args.get("artist")
        # Redirigir la petición al microservicio de letras
        response = requests.get(LYRICS_SERVICE_URL, params={"artist": artist})
        # Devolver la respuesta del microservicio en formato JSON
        return jsonify(response.json())
    else:
        # Si el token es inválido, devolver un mensaje de error
        return jsonify({"error": "Invalid token"}), 401


if __name__ == '__main__':
    app.run()


# Aquí se podrían definir otros endpoints para redirigir a otros microservicios

# To run this in a container:
# docker build -t gateway .