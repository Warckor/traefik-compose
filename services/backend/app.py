from flask import Flask
from flask_cors import CORS
import psycopg2
import os

POSTGRES_DB = os.getenv("POSTGRES_DB")
POSTGRES_USER = os.getenv("POSTGRES_USER")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
BACKEND_PORT = os.getenv("BACKEND_PORT")

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

@app.route('/data', methods=['GET'])
def hello():
    try:
        conn = psycopg2.connect(
            dbname=POSTGRES_DB, user=POSTGRES_USER, password=POSTGRES_PASSWORD, host="db"
        )
        return "Conexión a PostgreSQL exitosa"
    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=BACKEND_PORT)
