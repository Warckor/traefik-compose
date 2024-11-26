from flask import Flask
import psycopg2

app = Flask(__name__)

@app.route("/")
def hello():
    try:
        conn = psycopg2.connect(
            dbname="testdb", user="testuser", password="testpassword", host="db"
        )
        return "Conexión a PostgreSQL exitosa"
    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
