import oracledb
import json

with open("config.json", "r", encoding="utf-8") as f:
    config = json.load(f)

ORACLE_USER = config["ORACLE_USER"]
ORACLE_PASSWORD = config["ORACLE_PASSWORD"]
ORACLE_DSN = config["ORACLE_DSN"]

def conectar():
    return oracledb.connect(user=ORACLE_USER, password=ORACLE_PASSWORD, dsn=ORACLE_DSN)


def inserir_produtor(nome, cpf_cnpj, cidade, contato):
    with conectar() as conn:
        with conn.cursor() as cursor:
            cursor.execute("""
                INSERT INTO produtores (nome, cpf_cnpj, cidade, contato)
                VALUES (:1, :2, :3, :4)
            """, [nome, cpf_cnpj, cidade, contato])
            cursor.execute("SELECT MAX(id) FROM produtores")
            produtor_id = cursor.fetchone()[0]
            conn.commit()
            return produtor_id

def buscar_todos_produtores():
    with conectar() as conn:
        with conn.cursor() as cursor:
            cursor.execute("SELECT id, nome, cidade FROM produtores ORDER BY nome")
            return cursor.fetchall()

def buscar_produtor_por_id(produtor_id):
    with conectar() as conn:
        with conn.cursor() as cursor:
            cursor.execute("""
                SELECT nome, cpf_cnpj, cidade, contato
                FROM produtores
                WHERE id = :1
            """, [produtor_id])
            return cursor.fetchone()

def atualizar_produtor(produtor_id, nome, cpf_cnpj, cidade, contato):
    with conectar() as conn:
        with conn.cursor() as cursor:
            cursor.execute("""
                UPDATE produtores
                SET nome = :1, cpf_cnpj = :2, cidade = :3, contato = :4
                WHERE id = :5
            """, [nome, cpf_cnpj, cidade, contato, produtor_id])
            conn.commit()

def deletar_produtor(produtor_id):
    with conectar() as conn:
        with conn.cursor() as cursor:
            cursor.execute("DELETE FROM ofertas WHERE produtor_id = :1", [produtor_id])
            cursor.execute("DELETE FROM produtores WHERE id = :1", [produtor_id])
            conn.commit()

def inserir_oferta(produtor_id, produto, quantidade, preco, data_entrega):
    with conectar() as conn:
        with conn.cursor() as cursor:
            cursor.execute("""
                INSERT INTO ofertas (produtor_id, produto, quantidade, preco, data_entrega)
                VALUES (:1, :2, :3, :4, TO_DATE(:5, 'DD/MM/YYYY'))
            """, [produtor_id, produto, quantidade, preco, data_entrega])
            conn.commit()

def buscar_ofertas():
    with conectar() as conn:
        with conn.cursor() as cursor:
            cursor.execute("""
                SELECT o.produto, o.quantidade, o.preco,
                       TO_CHAR(o.data_entrega, 'DD/MM/YYYY'),
                       p.nome, p.cidade
                FROM ofertas o
                INNER JOIN produtores p ON o.produtor_id = p.id
                ORDER BY o.data_entrega
            """)
            return cursor.fetchall()

def buscar_ofertas_filtradas(cidade_filtro, produto_filtro, preco_max):
    with conectar() as conn:
        with conn.cursor() as cursor:
            query = """
                SELECT o.produto, o.quantidade, o.preco,
                       TO_CHAR(o.data_entrega, 'DD/MM/YYYY'),
                       p.nome, p.cidade
                FROM ofertas o
                INNER JOIN produtores p ON o.produtor_id = p.id
                WHERE 1=1
            """
            params = []
            if cidade_filtro:
                query += " AND LOWER(p.cidade) LIKE :1"
                params.append(f"%{cidade_filtro}%")
            if produto_filtro:
                query += f" AND LOWER(o.produto) LIKE :{len(params)+1}"
                params.append(f"%{produto_filtro}%")
            if preco_max is not None:
                query += f" AND o.preco <= :{len(params)+1}"
                params.append(preco_max)
            cursor.execute(query, params)
            return cursor.fetchall()

def inserir_comprador(nome, cpf, cidade, contato):
    with conectar() as conn:
        with conn.cursor() as cursor:
            cursor.execute("""
                INSERT INTO compradores (nome, cpf, cidade, contato)
                VALUES (:1, :2, :3, :4)
            """, [nome, cpf, cidade, contato])
            conn.commit()

def buscar_compradores_filtrados(cidade=None, nome=None):
    with conectar() as conn:
        with conn.cursor() as cursor:
            query = """
                SELECT nome, cpf, cidade, contato
                FROM compradores
                WHERE 1=1
            """
            params = []
            if cidade:
                query += " AND LOWER(cidade) LIKE :1"
                params.append(f"%{cidade}%")
            if nome:
                query += f" AND LOWER(nome) LIKE :{len(params)+1}"
                params.append(f"%{nome}%")
            cursor.execute(query, params)
            return cursor.fetchall()

