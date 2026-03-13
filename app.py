from flask import Flask
import psycopg2
import os

app = Flask(__name__)

def get_db():
    return psycopg2.connect(
        host=os.environ.get("DB_HOST", "db"),
        database=os.environ.get("DB_NAME", "mydb"),
        user=os.environ.get("DB_USER", "myuser"),
        password=os.environ.get("DB_PASSWORD", "mypassword")
    )

@app.route("/")
def hello():
    return "<h1>Hello from Flask + Docker!</h1>"

@app.route("/db")
def db_check():
    try:
        conn = get_db()
        conn.close()
        return "<h1>Database connection successful!</h1>"
    except Exception as e:
        return f"<h1>Database error: {e}</h1>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
