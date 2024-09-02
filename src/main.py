# src/main.py

from flask import Flask
from database.db import init_db

app = Flask(__name__)

@app.route('/')
def index():
    return "Bem-vindo ao sistema de monitoramento de saúde!"

if __name__ == '__main__':
    init_db()
    app.run(debug=True)