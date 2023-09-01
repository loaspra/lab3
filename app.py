from flask import Flask, request, jsonify
import pandas as pd

app = Flask(__name__)

# Cargar el CSV
data = pd.read_csv('spotify_millsongdata.csv')

@app.route('/obtener-letra', methods=['GET'])
def obtener_letra():
    cancion = request.args.get('cancion')
    # Buscar la canción
    cancion_encontrada = data[data['song'] == cancion]
    
    if cancion_encontrada.empty:
        return jsonify({'mensaje': 'Canción no encontrada'}), 404
    
    # Obtener la letra
    letra = cancion_encontrada['text'].values[0]
    
    return jsonify({'cancion': cancion, 'letra': letra})

if __name__ == '__main__':
    app.run()
