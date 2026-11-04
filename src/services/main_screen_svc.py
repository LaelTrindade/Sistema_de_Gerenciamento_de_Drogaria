from datetime import datetime

MESES = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho',
         'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']

def obter_data_hora():

    agora = datetime.now()

    data = f'{agora.day} de {MESES[agora.month - 1]} de {agora.year}'
    hora = agora.strftime('%H:%M')

    return data, hora