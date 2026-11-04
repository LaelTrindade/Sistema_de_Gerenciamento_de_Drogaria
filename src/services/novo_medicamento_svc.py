import sqlite3
from src.database.database_svc import conectar


def reais_para_centavos(texto):

    numeros = ''.join(c for c in texto if c.isdigit())

    return int(numeros) if numeros else 0


def salvar_dados_medicamento(nome, principio, laboratorio, categoria, preco):

    nome = nome.strip()
    principio = principio.strip()
    laboratorio = laboratorio.strip()
    categoria = categoria.strip()
    preco = preco.strip()

    if not all([nome, principio, laboratorio, preco]):
        return False, "Preencha todos os campos."

    try:
        with conectar() as conexao:
            conexao.execute("""--sql
                INSERT INTO medicamentos
                   (nome_comercial, principio_ativo, laboratorio, categoria, preco_centavos)
                   VALUES (?, ?, ?, ?, ?)""",
                (nome, principio, laboratorio, categoria, reais_para_centavos(preco))
            )

    except sqlite3.Error:
        return False, "Não foi possível salvar o medicamento."

    return True, "Medicamento salvo com sucesso!"