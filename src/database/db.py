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


    # Criar tabelas se não existirem
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS informacoes_demograficas (
        id SERIAL PRIMARY KEY,
        idade VARCHAR(20),
        genero VARCHAR(20),
        estado_civil VARCHAR(30),
        escolaridade VARCHAR(30),
        ocupacao VARCHAR(30),
        renda_mensal_familiar VARCHAR(30)
    );
    """)
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS condicoes_saude (
        id SERIAL PRIMARY KEY,
        estado_geral_saude VARCHAR(20),
        hipertensao BOOLEAN,
        diabetes BOOLEAN,
        asma BOOLEAN,
        doenca_cardiaca BOOLEAN,
        doenca_pulmonar BOOLEAN,
        doenca_renal BOOLEAN,
        cancer BOOLEAN,
        depressao BOOLEAN,
        nenhuma_condicao BOOLEAN
    );
    """)
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS habitos_vida (
        id SERIAL PRIMARY KEY,
        horas_sono VARCHAR(20),
        refeicoes_dia VARCHAR(20),
        atividade_fisica VARCHAR(20),
        alimentos_frescos VARCHAR(20),
        fuma VARCHAR(20),
        bebidas_alcoolicas VARCHAR(20)
    );
    """)
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS acesso_servicos_saude (
        id SERIAL PRIMARY KEY,
        acesso_comunidade BOOLEAN,
        frequencia_utilizacao VARCHAR(20),
        satisfacao_qualidade VARCHAR(20)
    );
    """)
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS avaliacao_geral (
        id SERIAL PRIMARY KEY,
        qualidade_vida_comunidade VARCHAR(20),
        problemas_qualidade_vida TEXT
    );
    """)

    conn.commit()
    cursor.close()
    conn.close()

def get_data():
    conn = psycopg2.connect(
        dbname='seu_banco',
        user='seu_usuario',
        password='sua_senha',
        host='localhost'
    )
    cursor = conn.cursor()

    # Coletar dados de todas as tabelas
    cursor.execute("SELECT * FROM informacoes_demograficas;")
    informacoes = cursor.fetchall()

    cursor.execute("SELECT * FROM condicoes_saude;")
    condicoes = cursor.fetchall()

    cursor.execute("SELECT * FROM habitos_vida;")
    habitos = cursor.fetchall()

    cursor.execute("SELECT * FROM acesso_servicos_saude;")
    acesso = cursor.fetchall()

    cursor.execute("SELECT * FROM avaliacao_geral;")
    avaliacao = cursor.fetchall()

    cursor.close()
    conn.close()

    return {
        'informacoes': informacoes,
        'condicoes': condicoes,
        'habitos': habitos,
        'acesso': acesso,
        'avaliacao': avaliacao
    }