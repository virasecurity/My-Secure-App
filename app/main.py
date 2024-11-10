# app/main.py
from flask import Flask, jsonify, request
from werkzeug.exceptions import BadRequest

app = Flask(__name__)

# Ruta para obtener un mensaje
@app.route('/api/message', methods=['GET'])
def get_message():
    return jsonify({"message": "Hello, secure world!"})

# Ruta para registrar datos con validación básica
@app.route('/api/register', methods=['POST'])
def register_data():
    try:
        data = request.get_json()
        if not data or 'name' not in data or 'email' not in data:
            raise BadRequest("Missing 'name' or 'email' fields.")
        
        # Aquí podríamos procesar o almacenar los datos de manera segura
        return jsonify({"message": "Data received successfully!"}), 201
    except BadRequest as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({"error": "An unexpected error occurred."}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
