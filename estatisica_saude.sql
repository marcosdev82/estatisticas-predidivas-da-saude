-- Tabela para armazenar informações demográficas
CREATE TABLE informacoes_demograficas (
    id SERIAL PRIMARY KEY,
    idade VARCHAR(20),
    genero VARCHAR(20),
    estado_civil VARCHAR(30),
    escolaridade VARCHAR(30),
    ocupacao VARCHAR(30),
    renda_mensal_familiar VARCHAR(30)
);

-- Tabela para armazenar condições de saúde
CREATE TABLE condicoes_saude (
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

-- Tabela para armazenar hábitos de vida
CREATE TABLE habitos_vida (
    id SERIAL PRIMARY KEY,
    horas_sono VARCHAR(20),
    refeicoes_dia VARCHAR(20),
    atividade_fisica VARCHAR(20),
    alimentos_frescos VARCHAR(20),
    fuma VARCHAR(20),
    bebidas_alcoolicas VARCHAR(20)
);

-- Tabela para armazenar acesso a serviços de saúde
CREATE TABLE acesso_servicos_saude (
    id SERIAL PRIMARY KEY,
    acesso_comunidade BOOLEAN,
    frequencia_utilizacao VARCHAR(20),
    satisfacao_qualidade VARCHAR(20)
);

-- Tabela para armazenar avaliação geral
CREATE TABLE avaliacao_geral (
    id SERIAL PRIMARY KEY,
    qualidade_vida_comunidade VARCHAR(20),
    problemas_qualidade_vida TEXT
);