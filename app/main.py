import sys
import os

# Obtiene el directorio en el que se encuentra main.py
current_dir = os.path.dirname(os.path.abspath(__file__))
# Obtiene el directorio raíz del proyecto, asumiendo que /app y /logger son hermanos
project_dir = os.path.dirname(current_dir)
# Agrega el directorio raíz del proyecto a sys.path
sys.path.append(project_dir)

from flask import Flask, request, jsonify
from logger.event_logger import EventloggerSidecar

app = Flask(__name__)

class Main:
    def __init__(self):
        self.event_logger = EventloggerSidecar()

    def process_message(self, message):
        print(f"Processing message: {message}")
        # Utilizando el sidecar para registrar un evento
        self.event_logger.log_event(f"Message processed: {message}")

@app.route('/process', methods=['POST'])
def process():
    data = request.json
    message = data.get('message', '')
    if message:
        main_app.process_message(message)
        return jsonify({"status": "success", "message": "Message processed"}), 200
    else:
        return jsonify({"status": "error", "message": "No message provided"}), 400

if __name__ == '__main__':
    main_app = Main()
    app.run(debug=True)