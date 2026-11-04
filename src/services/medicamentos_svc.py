import sqlite3
import unicodedata
from src.database.database_svc import conectar


def normalizar(texto):

    sem_acento = unicodedata.normalize('NFKD', texto).encode('ascii', 'ignore').decode('ascii')

    return sem_acento.casefold()


def chave_ordenacao(medicamento):

    return normalizar(medicamento.get('nome_comercial', ''))


def centavos_para_reais(centavos):

    reais, resto = divmod(centavos, 100)

    return f'R$ {reais:,}'.replace(',', '.') + f',{resto:02d}'


def carregar_medicamentos():

    try:

        with conectar() as conexao:

            linhas = conexao.execute('SELECT * FROM medicamentos').fetchall()

    except sqlite3.Error:

        return []

    lista = []

    for linha in linhas:

        medicamento = dict(linha)
        medicamento['preco'] = centavos_para_reais(medicamento['preco_centavos'])

        lista.append(medicamento)

    return sorted(lista, key = chave_ordenacao)


def excluir_medicamento(id_medicamento):

    with conectar() as conexao:

        cursor = conexao.execute('DELETE FROM medicamentos WHERE id = ?', (id_medicamento,))

        apagou = cursor.rowcount > 0

    return apagou


def buscar_medicamentos(termo = '', categoria = '', laboratorio = ''):

    termo = normalizar(termo.strip())

    resultado = []

    for medicamento in carregar_medicamentos():

        campos = [
            medicamento.get('nome_comercial', ''),
            medicamento.get('principio_ativo', '')
        ]

        if termo and not any(termo in normalizar(campo) for campo in campos):

            continue

        if categoria and medicamento.get('categoria', '') != categoria:

            continue

        if laboratorio and normalizar(medicamento.get('laboratorio', '').strip()) != normalizar(laboratorio):

            continue

        resultado.append(medicamento)

    return resultado


def listar_laboratorios():

    laboratorios = {}

    for medicamento in carregar_medicamentos():

        laboratorio = medicamento.get('laboratorio', '').strip()

        if laboratorio:

            laboratorios.setdefault(normalizar(laboratorio), laboratorio)

    return sorted(laboratorios.values(), key = normalizar)