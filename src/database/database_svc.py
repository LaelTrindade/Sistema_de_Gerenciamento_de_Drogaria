import sqlite3
from contextlib import contextmanager
from src.config.paths import CAMINHO_DATABASE


@contextmanager
def conectar():

    conexao = sqlite3.connect(CAMINHO_DATABASE)
    conexao.row_factory = sqlite3.Row
    conexao.execute('PRAGMA foreign_keys = ON')

    try:
        yield conexao
        conexao.commit()

    except Exception:
        conexao.rollback()
        raise

    finally:
        conexao.close()


def criar_tabelas():

    with conectar() as conexao:

        conexao.execute("""--sql
            CREATE TABLE IF NOT EXISTS medicamentos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome_comercial TEXT NOT NULL,
                principio_ativo TEXT NOT NULL,
                laboratorio TEXT NOT NULL,
                categoria TEXT NOT NULL,
                preco_centavos INTEGER NOT NULL
            )
        """)

        conexao.execute("""--sql
            CREATE TABLE IF NOT EXISTS usuarios (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                login TEXT NOT NULL UNIQUE COLLATE NOCASE,
                senha_hash TEXT NOT NULL,
                perfil TEXT NOT NULL,
                ativo INTEGER NOT NULL DEFAULT 1
            )
        """)

        conexao.execute("""--sql
            INSERT INTO usuarios (nome, login, senha_hash, perfil, ativo)
            SELECT 'Administrador', 'administrador',
                   '$2b$12$uwM.P3iNBJg2zp.RrFZcreHjPKvvJsJBBRDQjb9okkkrHhysfyWMa',
                   'admin', 1
            WHERE NOT EXISTS (SELECT 1 FROM usuarios)
        """)