import customtkinter as ctk
from PIL import Image
from src.config.paths import IMAGES_MEDICAMENTOS
from src.views.novo_medicamento_vws import exibir_novo_medicamento
from src.services.medicamentos_svc import buscar_medicamentos, listar_laboratorios, excluir_medicamento
from src.views.messagebox_vws import exibir_messagebox, MODO_SUCESSO, MODO_ERRO, MODO_BOOLEANO


#           Nome  Princ.  Lab.  Cat.  Estoque  Preço  Ações
LARGURAS = [245,   170,   170,  190,    85,    120,    90]
PESOS    = [  6,     4,     4,    3,     2,      3,     2]

TODAS_CATEGORIAS = 'Todas as categorias'
TODOS_LABORATORIOS = 'Todos os laboratórios'


def configurar_colunas(frame):

    for i, (largura, peso) in enumerate(zip(LARGURAS, PESOS)):

        frame.grid_columnconfigure(i, minsize = largura, weight = peso)


def obter_icone_estoque(quantidade):

    if quantidade <= 5:

        return 'red_circle.png'

    if quantidade <= 15:

        return 'yellow_circle.png'

    return 'green_circle.png'


def criar_imagem(arquivo, tamanho):

    imagem = Image.open(IMAGES_MEDICAMENTOS/arquivo)

    return ctk.CTkImage(light_image = imagem, dark_image = imagem, size = (tamanho, tamanho))


def excluir_linha(linha, medicamento):

    janela = linha.winfo_toplevel()

    def confirmar_exclusao():

        if excluir_medicamento(medicamento['id']):

            linha.destroy()

            exibir_messagebox(janela, MODO_SUCESSO, 'Medicamento excluído com sucesso!')

        else:

            exibir_messagebox(janela, MODO_ERRO, 'Não foi possível excluir o medicamento.')

    exibir_messagebox(janela, MODO_BOOLEANO, f"Deseja excluir o medicamento {medicamento['nome_comercial']}?", confirmar_exclusao)


def criar_linha(parent, medicamento, indice):

    conteudo_frame = ctk.CTkFrame(
        master = parent,
        height = 75,
        border_width = 1,
        corner_radius = 0,
        fg_color = '#FFFFFF',
        border_color = '#DCE6EE'
    )

    conteudo_frame.grid(row = indice, column = 0, sticky = 'ew')

    configurar_colunas(conteudo_frame)

    label_nome = ctk.CTkLabel(
        master = conteudo_frame,
        width = 0,
        height = 0,
        anchor = 'w',
        compound = 'left',
        font = ('Inter', 14),
        text = f"  {medicamento['nome_comercial']}",
        text_color = '#18344A',
        image = criar_imagem('pill_icon.png', 26)
    )

    label_nome.grid(row = 0, column = 0, sticky = 'w', padx = (20, 0), pady = 20)


    ativo = medicamento['principio_ativo']

    if len(ativo) > 20:

        ativo = ativo[:19].rstrip() + '…'

    textos = [
        (1, ativo),
        (2, medicamento['laboratorio']),
        (3, medicamento['categoria']),
        (5, medicamento['preco'])
    ]


    for coluna, texto in textos:

        label = ctk.CTkLabel(
            master = conteudo_frame,
            width = 0,
            height = 0,
            anchor = 'w',
            font = ('Inter', 14),
            text = texto,
            text_color = '#18344A'
        )

        label.grid(row = 0, column = coluna, sticky = 'w', pady = 20)

    estoque = medicamento.get('estoque', 0)

    label_estoque = ctk.CTkLabel(
        master = conteudo_frame,
        width = 0,
        height = 0,
        anchor = 'w',
        compound = 'left',
        font = ('Inter', 14),
        text = f'  {estoque}',
        text_color = '#18344A',
        image = criar_imagem(obter_icone_estoque(estoque), 12)
    )

    label_estoque.grid(row = 0, column = 4, sticky = 'w', pady = 20)

    frame_acoes = ctk.CTkFrame(
        master = conteudo_frame,
        fg_color = 'transparent'
    )

    frame_acoes.grid(row = 0, column = 6, sticky = 'w', pady = 20)

    button_edit = ctk.CTkButton(
        master = frame_acoes,
        width = 25,
        height = 25,
        corner_radius = 5,
        fg_color = '#FFFFFF',
        hover_color = '#F5F8FC',
        text = '',
        image = criar_imagem('pencil_icon.png', 21)
    )

    button_edit.grid(row = 0, column = 0)

    button_delete = ctk.CTkButton(
        master = frame_acoes,
        width = 25,
        height = 25,
        corner_radius = 5,
        fg_color = '#FFFFFF',
        hover_color = '#F5F8FC',
        text = '',
        image = criar_imagem('trash_icon.png', 21),
        command = lambda: excluir_linha(conteudo_frame, medicamento)
    )

    button_delete.grid(row = 0, column = 1, padx = (5, 0))


def preencher_linhas(frame_linhas, termo = '', categoria = '', laboratorio = ''):

    for widget in frame_linhas.winfo_children():

        widget.destroy()

    for indice, medicamento in enumerate(buscar_medicamentos(termo, categoria, laboratorio)):

        criar_linha(frame_linhas, medicamento, indice)


def exibir_medicamentos(frame_parent):

    frame_parent.grid_columnconfigure(0, weight = 0)
    frame_parent.grid_columnconfigure(1, weight = 1)
    frame_parent.grid_rowconfigure(2, weight = 1)

    frame_titulos = ctk.CTkFrame(
        master = frame_parent,
        fg_color = 'transparent'
    )
    frame_titulos.grid(row = 0, column = 0, sticky = 'nw', padx = 30, pady = (20, 0))

    title = ctk.CTkLabel(
        master = frame_titulos,
        width = 0,
        height = 0,
        text_color = '#18344A',
        font = ('Inter', 24, 'bold'),
        text = 'Medicamentos'
    )
    title.grid(row = 0, column = 0, sticky = 'w')

    subtext = ctk.CTkLabel(
        master = frame_titulos,
        width = 0,
        height = 0,
        text_color = '#60788A',
        font = ('Inter', 14),
        text = 'Gerência, cadastro e informações de seus medicamentos.'
    )
    subtext.grid(row = 1, column = 0, sticky = 'w', pady = (2, 0))

    add_medicament = ctk.CTkButton(
        master = frame_parent,
        width = 230,
        height = 50,
        cursor = 'hand2',
        corner_radius = 5,
        compound = 'left',
        font = ('Inter', 16, 'bold'),
        text = ' Novo Medicamento',
        text_color = '#FFFFFF',
        fg_color = '#1C6EA4',
        hover_color = '#155A87',
        image = ctk.CTkImage(
            light_image = Image.open(IMAGES_MEDICAMENTOS/'plus_icon.png'),
            dark_image = Image.open(IMAGES_MEDICAMENTOS/'plus_icon.png'),
            size = (24, 24)
        ),
        command = lambda: exibir_novo_medicamento(frame_parent.master, lambda: ao_cadastrar())
    )
    add_medicament.grid(row = 0, column = 1, sticky = 'ne', padx = 30, pady = (20, 0))


# Início frame_cards

    frame_cards = ctk.CTkFrame(
        master = frame_parent,
        fg_color = 'transparent'
    )
    frame_cards.grid(row = 1, column = 0, sticky = 'new', padx = (30, 25), pady = (20, 0), columnspan = 2)

    # Início frame_pesquisa + widgets
    frame_pesquisa = ctk.CTkFrame(
        master = frame_cards,
        width = 656,
        height = 40,
        border_width = 1,
        corner_radius = 5,
        fg_color = '#FFFFFF',
        border_color = '#D9E3EC'
    )

    frame_pesquisa.grid(row = 0, column = 0, sticky = 'nw')
    frame_pesquisa.pack_propagate(False)

    search_icon = ctk.CTkLabel(
        master = frame_pesquisa,
        width = 0,
        height = 0,
        text = '',
        image = ctk.CTkImage(
            light_image = Image.open(IMAGES_MEDICAMENTOS/'search_icon.png'),
            dark_image = Image.open(IMAGES_MEDICAMENTOS/'search_icon.png'),
            size = (21, 21)
        )
    )

    search_icon.pack(side = 'left', padx = (12, 4))

    entry_1 = ctk.CTkEntry(
        master = frame_pesquisa,
        width = 635,
        height = 35,
        corner_radius = 0,
        border_width = 0,
        font = ('Inter', 14),
        text_color = '#1E293B',
        fg_color = 'transparent',
        placeholder_text = 'Pesquisar por nome ou princípio ativo...',
        placeholder_text_color = '#94A3B8'
    )

    entry_1.pack(side = 'left', padx = (0, 5))
    # Fim frame_pesquisa + widgets

    # Início frame_categoria + widgets
    frame_categoria = ctk.CTkFrame(
        master = frame_cards,
        width = 200,
        height = 40,
        border_width = 1,
        corner_radius = 5,
        fg_color = '#FFFFFF',
        border_color = '#D9E3EC'
    )

    frame_categoria.grid(row = 0, column = 1, padx = 10, sticky = 'nw')
    frame_categoria.pack_propagate(False)

    option_categorias = [
        'Todas as categorias',
        'Analgésico / Antitérmico',
        'Anti-inflamatório',
        'Antibiótico',
        'Antialérgico',
        'Vitamina / Suplemento',
        'Outro',
    ]

    option_menu_1 = ctk.CTkOptionMenu(
        master = frame_categoria,
        values = option_categorias,
        width = 180,
        height = 30,
        cursor = 'hand2',
        font = ('Inter', 14),
        fg_color = '#FFFFFF',
        button_color = '#FFFFFF',
        button_hover_color = '#E9F0F7',
        text_color = '#1E293B',
        dropdown_font = ('Inter', 14),
        dropdown_fg_color = '#FFFFFF',
        dropdown_hover_color = '#E9F0F7',
        dropdown_text_color = '#94A3B8'
    )

    option_menu_1.pack(padx = 5, pady = 5)
    # Fim frame_categoria + widgets

    # Início frame_laboratório + widgets
    frame_laboratorio = ctk.CTkFrame(
        master = frame_cards,
        width = 210,
        height = 40,
        border_width = 1,
        corner_radius = 5,
        fg_color = '#FFFFFF',
        border_color = '#D9E3EC'
    )

    frame_laboratorio.grid(row = 0, column = 2, sticky = 'nw', padx = (0, 2))
    frame_laboratorio.pack_propagate(False)

    option_menu_2 = ctk.CTkOptionMenu(
        master = frame_laboratorio,
        values = [TODOS_LABORATORIOS] + listar_laboratorios(),
        width = 190,
        height = 30,
        cursor = 'hand2',
        font = ('Inter', 14),
        fg_color = '#FFFFFF',
        button_color = '#FFFFFF',
        button_hover_color = '#E9F0F7',
        text_color = '#1E293B',
        dropdown_font = ('Inter', 14),
        dropdown_fg_color = '#FFFFFF',
        dropdown_hover_color = '#E9F0F7',
        dropdown_text_color = '#94A3B8'
    )

    option_menu_2.pack(padx = 5, pady = 5)
    # Fim frame_laboratório + widgets

# Fim frame_cards



# Início main_frame
    main_frame = ctk.CTkScrollableFrame(
        master = frame_parent,
        corner_radius = 5,
        border_width = 1,
        fg_color = '#F5F8FC',
        border_color = '#DCE6EE'
    )

    main_frame.grid(row = 2, column = 0, sticky = 'nsew', padx = 30, pady = (20, 10), columnspan = 2)
    main_frame._scrollbar.grid_configure(padx = (0, 2), pady = (58, 10))

    configurar_colunas(main_frame)

    # Início colunas do main_frame
    titulos_colunas = [
        'Nome do Medicamento',
        'Princípio Ativo',
        'Laboratório',
        'Categoria',
        'Estoque',
        'Preço',
        'Ações'
    ]

    for i, texto in enumerate(titulos_colunas):

        titulo_coluna = ctk.CTkLabel(
            master = main_frame,
            width = 0,
            height = 0,
            anchor = 'w',
            font = ('Inter', 14, 'bold'),
            text = texto,
            text_color = '#18344A'
        )

        titulo_coluna.grid(row = 0, column = i, sticky = 'w', padx = (20, 0) if i == 0 else 0, pady = 20)
    # Fim colunas do main_frame



    # Início frame_linhas
    frame_linhas = ctk.CTkFrame(
        master = main_frame,
        height = 0,
        fg_color = 'transparent'
    )

    frame_linhas.grid(row = 1, column = 0, sticky = 'new', padx = (0, 10), columnspan = len(LARGURAS))
    frame_linhas.grid_columnconfigure(0, weight = 1)

    preencher_linhas(frame_linhas)

    def atualizar_lista(*args):

        categoria = option_menu_1.get()
        laboratorio = option_menu_2.get()

        if categoria == TODAS_CATEGORIAS:

            categoria = ''

        if laboratorio == TODOS_LABORATORIOS:

            laboratorio = ''

        preencher_linhas(frame_linhas, entry_1.get(), categoria, laboratorio)


    def atualizar_laboratorios():

        valores = [TODOS_LABORATORIOS] + listar_laboratorios()

        option_menu_2.configure(values = valores)

        if option_menu_2.get() not in valores:

            option_menu_2.set(TODOS_LABORATORIOS)


    def ao_cadastrar():

        if not frame_linhas.winfo_exists():

            return

        atualizar_laboratorios()
        atualizar_lista()


    entry_1.bind('<KeyRelease>', atualizar_lista)
    option_menu_1.configure(command = atualizar_lista)
    option_menu_2.configure(command = atualizar_lista)