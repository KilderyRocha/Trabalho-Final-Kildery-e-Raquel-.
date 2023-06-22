import psycopg2


def conectar_banco():
    conn = psycopg2.connect(database="AltisTelecom", user="postgres", password="postgre", host="localhost")
    return conn


def criar_tabelas(conn):
    cursor = conn.cursor()

    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS clientes (
            id SERIAL PRIMARY KEY,
            nome VARCHAR(100) NOT NULL,
            email VARCHAR(100) NOT NULL UNIQUE,
            telefone VARCHAR(20) NOT NULL
        );
    ''')

    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS planos (
            id SERIAL PRIMARY KEY,
            nome VARCHAR(100) NOT NULL,
            preco NUMERIC(10, 2) NOT NULL,
            velocidade INTEGER NOT NULL
        );
    ''')

    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS vendas (
            id SERIAL PRIMARY KEY,
            cliente_id INTEGER REFERENCES clientes(id),
            plano_id INTEGER REFERENCES planos(id),
            data_venda DATE NOT NULL,
            valor NUMERIC(10, 2) NOT NULL
        );
    ''')

    conn.commit()
    cursor.close()


conn = conectar_banco()
criar_tabelas(conn)
conn.close()
