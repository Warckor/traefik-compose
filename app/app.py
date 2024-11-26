from flask import Flask
import psycopg2
from dotenv import load_dotenv
import os

load_dotenv()

POSTGRES_DB = os.getenv("POSTGRES_DB")
POSTGRES_USER = os.getenv("POSTGRES_USER")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")

app = Flask(__name__)

@app.route("/")
def hello():
    try:
        conn = psycopg2.connect(
            dbname=POSTGRES_DB, user=POSTGRES_USER, password=POSTGRES_PASSWORD, host="db"
        )
        return "Conexión a PostgreSQL exitosa"
    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
