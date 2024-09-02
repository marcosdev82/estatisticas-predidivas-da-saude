# src/database/db.py

import psycopg2
from psycopg2 import sql

def init_db():
    conn = psycopg2.connect(
        dbname='seu_banco',
        user='seu_usuario',
        password='sua_senha',
        host='localhost'
    )
    cursor = conn.cursor()
    
    # Criar tabela de usuários
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS usuarios (
        id SERIAL PRIMARY KEY,
        nome VARCHAR(100) NOT NULL,
        email VARCHAR(100) UNIQUE NOT NULL,
        senha VARCHAR(255) NOT NULL,
        nivel_acesso VARCHAR(20) NOT NULL,
        data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        ultimo_acesso TIMESTAMP
    );
    """)
    
    conn.commit()
    cursor.close()
    conn.close()