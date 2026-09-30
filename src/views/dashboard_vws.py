import customtkinter as ctk
from PIL import Image
from src.config.paths import IMAGES_DASHBOARD
from src.controllers.dashboard_controller import obter_dados_dashboard


def exibir_dashboard(frame_parent):

    frame_parent.grid_columnconfigure(1, weight = 1)

    frame_parent.grid_rowconfigure(3, weight = 1)
    frame_parent.grid_rowconfigure(4, weight = 1)

    
    (
            faturamento,
            medicamentos,
            estoque,
            alertas,
            dias_semana,
            valores_vendas,
            relatorios,

    ) = obter_dados_dashboard()


    hello_user = ctk.CTkLabel(
        master = frame_parent,
        width = 0,
        height = 0,
        text_color = '#18344A',
        font = ('Inter', 24, 'bold'),
        text = 'Olá, Administrador!'
    )

    hello_user.grid(row = 0, column = 0, sticky = 'nw', padx = 30, pady = (20, 0), columnspan = 2)

    subtext = ctk.CTkLabel(
        master = frame_parent,
        width = 0,
        height = 0,
        text_color = '#60788A',
        font = ('Inter', 14),
        text = 'Confira sua drogaria e acompanhe seus resultados.'
    )

    subtext.grid(row = 1, column = 0, sticky = 'nw', padx = 30, pady = 2, columnspan = 2)

# Fim [Texto Auxiliar]


# Início [Frame Cards]

    fr_cards = ctk.CTkFrame(
        master = frame_parent,
        fg_color = 'transparent'
    )

    fr_cards.grid(row = 2, column = 0, sticky = 'new', padx = (30, 0), pady = (15, 0))



    card_vendas = ctk.CTkFrame(
        master = fr_cards,
        width = 220,
        height = 140,
        border_width = 1,
        corner_radius = 5,
        fg_color = '#FFFFFF',
        border_color = '#E2EAF1'
    )

    card_vendas.grid_propagate(False)
    card_vendas.grid(row = 0, column = 0, sticky = 'w')

    # Início [Elementos - Card de Vendas]

    cash_icon = ctk.CTkLabel(
        master = card_vendas,
        width = 0,
        height = 0,
        text = '',
        image = ctk.CTkImage(
            light_image = Image.open(IMAGES_DASHBOARD/'teste_icon.png'),
            dark_image = Image.open(IMAGES_DASHBOARD/'teste_icon.png'),
            size = ((28, 28))
        )
    )

    cash_icon.grid(row = 0, column = 0, sticky = 'nw', padx = 20, pady = (20, 0))

    lb_card_vendas = ctk.CTkLabel(
        master = card_vendas,
        width = 0,
        height = 0,
        font = ('Inter', 12),
        text = 'Faturamento'
    )

    lb_card_vendas.grid(row = 1, column = 0, sticky = 'w', padx = 20, pady = (35, 0))

    lb2_card_vendas = ctk.CTkLabel(
        master = card_vendas,
        width = 0,
        height = 0,
        font = ('Inter', 18, 'bold'),
        text = faturamento
    )

    lb2_card_vendas.grid(row = 2, column = 0, sticky = 'w', padx = 20, pady = (3, 0))

    # Fim [Elementos - Card de Vendas]



    card_medicamentos = ctk.CTkFrame(
        master = fr_cards,
        width = 220,
        height = 140,
        border_width = 1,
        corner_radius = 5,
        fg_color = '#FFFFFF',
        border_color = '#E2EAF1'
    )

    card_medicamentos.grid_propagate(False)
    card_medicamentos.grid(row = 0, column = 1, sticky = 'w', padx = 10)

    # Início [Elementos - Card de Medicamentos]

    pills_icon = ctk.CTkLabel(
        master = card_medicamentos,
        width = 0,
        height = 0,
        text = '',
        image = ctk.CTkImage(
            light_image = Image.open(IMAGES_DASHBOARD/'teste_icon.png'),
            dark_image = Image.open(IMAGES_DASHBOARD/'teste_icon.png'),
            size = ((28, 28))
        )
    )

    pills_icon.grid(row = 0, column = 0, sticky = 'nw', padx = 20, pady = (20, 0))

    lb_card_medicamentos = ctk.CTkLabel(
        master = card_medicamentos,
        width = 0,
        height = 0,
        font = ('Inter', 12),
        text = 'Medicamentos vendidos'
    )

    lb_card_medicamentos.grid(row = 1, column = 0, sticky = 'w', padx = 20, pady = (35, 0))

    lb2_card_medicamentos = ctk.CTkLabel(
        master = card_medicamentos,
        width = 0,
        height = 0,
        font = ('Inter', 18, 'bold'),
        text = medicamentos,
    )

    lb2_card_medicamentos.grid(row = 2, column = 0, sticky = 'w', padx = 20, pady = (3, 0))

    # Fim [Elementos - Card de Medicamentos]



    card_estoque = ctk.CTkFrame(
        master = fr_cards,
        width = 220,
        height = 140,
        border_width = 1,
        corner_radius = 5,
        fg_color = '#FFFFFF',
        border_color = '#E2EAF1'
    )

    card_estoque.grid_propagate(False)
    card_estoque.grid(row = 0, column = 2, sticky = 'w')

    # Início [Elementos - Card de Estoque]

    box_icon = ctk.CTkLabel(
        master = card_estoque,
        width = 0,
        height = 0,
        text = '',
        image = ctk.CTkImage(
            light_image = Image.open(IMAGES_DASHBOARD/'teste_icon.png'),
            dark_image = Image.open(IMAGES_DASHBOARD/'teste_icon.png'),
            size = ((28, 28))
        )
    )

    box_icon.grid(row = 0, column = 0, sticky = 'nw', padx = 20, pady = (20, 0))

    lb_card_estoque = ctk.CTkLabel(
        master = card_estoque,
        width = 0,
        height = 0,
        font = ('Inter', 12),
        text = 'Itens em estoque'
    )

    lb_card_estoque.grid(row = 1, column = 0, sticky = 'w', padx = 20, pady = (35, 0))

    lb2_card_estoque = ctk.CTkLabel(
        master = card_estoque,
        width = 0,
        height = 0,
        font = ('Inter', 18, 'bold'),
        text = estoque,
    )

    lb2_card_estoque.grid(row = 2, column = 0, sticky = 'w', padx = 20, pady = (3, 0))

    # Fim [Elementos - Card de Estoque]


# Início [ Frame de Acesso Rápido]

    fr_quick_acess = ctk.CTkFrame(
        master = frame_parent,
        height = 300,
        border_width = 1,
        corner_radius = 5,
        fg_color = '#FFFFFF',
        border_color = '#E2EAF1'
    )

    fr_quick_acess.grid_propagate(False)
    fr_quick_acess.grid_columnconfigure(0, weight = 1)
    fr_quick_acess.grid_rowconfigure(1, weight = 1)

    fr_quick_acess.grid(row = 2, column = 1, sticky = 'nsew', padx = (10, 20), pady = (15, 0), rowspan = 2)

    lb_quick_acess = ctk.CTkLabel(
        master = fr_quick_acess,
        width = 0,
        height = 0,
        anchor = 'w',
        compound = 'left',
        font = ('Inter', 14, 'bold'),
        text = '  Acesso rápido - Relatórios',
        image = ctk.CTkImage(
            light_image = Image.open(IMAGES_DASHBOARD/'clock_icon.png'),
            dark_image = Image.open(IMAGES_DASHBOARD/'clock_icon.png'),
            size = ((22, 22))
        )
    )

    lb_quick_acess.grid(row = 0, column = 0, sticky = 'nw', padx = 15, pady = (12, 2))

    sf_relatorios = ctk.CTkScrollableFrame(
        master = fr_quick_acess,
        corner_radius = 2,
        fg_color = '#F5F8FC'
    )

    sf_relatorios.grid(row = 1, column = 0, sticky = 'nsew', padx = 5, pady = 5)

    sf_relatorios.grid_columnconfigure(0, weight = 4, uniform = 'rel')
    sf_relatorios.grid_columnconfigure(1, weight = 2, uniform = 'rel')
    sf_relatorios.grid_columnconfigure(2, weight = 3, uniform = 'rel')
    sf_relatorios.grid_columnconfigure(3, weight = 3, uniform = 'rel')


    # Início - [Elementos do Scrollable Frame de Relatórios]

    column_produto = ctk.CTkLabel(
        master = sf_relatorios,
        width = 0,
        height = 20,
        corner_radius = 5,
        fg_color = '#B8DCEC',
        text_color = '#18344A',
        font = ('Inter', 12, 'bold'),
        text = 'Produto'
    )

    column_produto.grid(row = 0, column = 0, sticky = 'new', padx = 5, pady = 5)

    column_quantidade = ctk.CTkLabel(
        master = sf_relatorios,
        width = 0,
        height = 20,
        corner_radius = 5,
        fg_color = '#B8DCEC',
        text_color = '#18344A',
        font = ('Inter', 12, 'bold'),
        text = 'Qtde.'
    )

    column_quantidade.grid(row = 0, column = 1, sticky = 'new', pady = 5)

    column_valor = ctk.CTkLabel(
        master = sf_relatorios,
        width = 0,
        height = 20,
        corner_radius = 5,
        fg_color = '#B8DCEC',
        text_color = '#18344A',
        font = ('Inter', 12, 'bold'),
        text = 'Valor'
    )

    column_valor.grid(row = 0, column = 2, sticky = 'new', padx = 5, pady = 5)

    column_horario = ctk.CTkLabel(
        master = sf_relatorios,
        width = 0,
        height = 20,
        corner_radius = 5,
        fg_color = '#B8DCEC',
        text_color = '#18344A',
        font = ('Inter', 12, 'bold'),
        text = 'Horário'
    )

    column_horario.grid(row = 0, column = 3, sticky = 'new', pady = 5)

# Início [Listagem de Relatórios]
    for i, (produto, quantidade, valor, horario) in enumerate(relatorios):
        produto_texto = produto if len(produto) <= 14 else produto[:12] + '...'

        lb_produto = ctk.CTkLabel(
            master = sf_relatorios,
            width = 0,
            height = 20,
            anchor = 'w',
            text = produto_texto
        )
        lb_produto.grid(row = i + 1, column = 0, sticky = 'new', padx = (15, 5), pady = 2)

        lb_quantidade = ctk.CTkLabel(
            master = sf_relatorios,
            width = 65,
            height = 20,
            text = str(quantidade)
        )
        lb_quantidade.grid(row = i + 1, column = 1, sticky = 'new', pady = 2)

        lb_valor = ctk.CTkLabel(
            master = sf_relatorios,
            width = 90,
            height = 20,
            text = f'R$ {float(valor):.2f}'
        )
        lb_valor.grid(row = i + 1, column = 2, sticky = 'new', padx = 5, pady = 2)

        lb_horario = ctk.CTkLabel(
            master = sf_relatorios,
            width = 80,
            height = 20,
            text = str(horario)
        )
        lb_horario.grid(row = i + 1, column = 3, sticky = 'new', pady = 2)
        # Fim [Listagem de Relatórios].

    
# Início [Frame de Alertas].

    fr_alertas = ctk.CTkFrame(
        master = frame_parent,
        height = 240,
        corner_radius = 5,
        border_width = 1,
        fg_color = '#FFF1F1',
        border_color = '#F3B8BA'
    )

    fr_alertas.grid_propagate(False)

    fr_alertas.grid_columnconfigure(0, weight = 1)
    fr_alertas.grid_rowconfigure(1, weight = 1)

    fr_alertas.grid(row = 4, column = 1, sticky = 'nsew', padx = (10, 20), pady = 10)

    bell_icon = ctk.CTkLabel(
        master = fr_alertas,
        width = 0,
        height = 0,
        anchor = 'w',
        compound = 'left',
        text = '  Alertas',
        text_color = '#8F252A',
        font = ('Inter', 14, 'bold'),
        image = ctk.CTkImage(
            light_image = Image.open(IMAGES_DASHBOARD/'bell_icon.png'),
            dark_image = Image.open(IMAGES_DASHBOARD/'bell_icon.png'),
            size = ((22, 22))
        )
    )

    bell_icon.grid(row = 0, column = 0, sticky = 'nw', padx = 15, pady = (15, 0))


    # Início [Widgets do Frame de Alertas].

    fr_transparent = ctk.CTkFrame(
        master = fr_alertas,
        corner_radius = 2,
        fg_color = '#FFCCCE'
    )

    fr_transparent.grid(row = 1, column = 0, sticky = 'nsew', padx = 10, pady = 10)

    for i, texto in enumerate(alertas[:3]):

        alert_titulo = ctk.CTkLabel(
            master = fr_transparent,
            width = 0,
            height = 0,
            anchor = 'w',
            compound = 'left',
            font = ('Inter', 14, 'bold'),
            text = '  Medicamento com estoque baixo',
            image = ctk.CTkImage(
                light_image = Image.open(IMAGES_DASHBOARD/'warning_icon.png'),
                dark_image = Image.open(IMAGES_DASHBOARD/'warning_icon.png'),
                size = (20, 20)
            )
        )

        alert_titulo.grid(row = i * 2, column = 0, sticky = 'new', padx = 10, pady = (10, 0))

        alert_detalhe = ctk.CTkLabel(
            master = fr_transparent,
            width = 0,
            height = 0,
            anchor = 'w',
            font = ('Inter', 12),
            text = f'• {texto}'
        )

        alert_detalhe.grid(row = i * 2 + 1, column = 0, sticky = 'new', padx = 35, pady = (2, 10))

    # Fim [Widgets do Frame de Alertas].

# Fim [Frame de Alertas].


# Início [Frame de Gráfico de Vendas]

    graphic = ctk.CTkFrame(
        master = frame_parent,
        corner_radius = 5,
        border_width = 1,
        fg_color = '#FFFFFF',
        border_color = '#E2EAF1'
    )

    graphic.grid(row = 3, column = 0, sticky = 'nsew', padx = (30, 0), pady = 10, rowspan = 2)

    lb_graphic = ctk.CTkLabel(
        master = graphic,
        width = 0,
        height = 0,
        anchor = 'w',
        font = ('Inter', 16, 'bold'),
        text = 'Vendas da Semana'
    )

    lb_graphic.grid(row = 0, column = 0, sticky = 'new', padx = 20, pady = (15, 5))


    # Início [Elementos Genéricos para o gráfico] // Feito com IA
    from matplotlib.figure import Figure
    from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
    import numpy as np

    dias = dias_semana
    vendas = valores_vendas

    fig = Figure(figsize = (5, 2.2), dpi = 100)
    fig.patch.set_facecolor('#FFFFFF')

    ax = fig.add_subplot(111)
    ax.set_facecolor('#FFFFFF')

    for spine in ax.spines.values():
        spine.set_visible(False)

    ax.tick_params(length = 0, colors = '#60788A', labelsize = 9)
    ax.set_xticks(range(len(dias)))
    ax.set_xticklabels(dias)

    ax.grid(axis = 'y', color = '#E2EAF1', linewidth = 0.8)
    ax.set_axisbelow(True)

    cor_linha = '#1C6EA4'

    ax.plot(dias, vendas, color = cor_linha, linewidth = 2, marker = 'o', markersize = 5, markerfacecolor = '#FFFFFF', markeredgecolor = cor_linha, markeredgewidth = 1.5)
    ax.fill_between(dias, vendas, color = cor_linha, alpha = 0.08)

    ax.set_ylim(bottom = 0)
    fig.tight_layout(pad = 1.5)

    canvas_grafico = FigureCanvasTkAgg(fig, master = graphic)
    canvas_grafico.draw()
    canvas_grafico.get_tk_widget().grid(row = 1, column = 0, sticky = 'nsew', padx = 15, pady = (5, 15))

    graphic.grid_columnconfigure(0, weight = 1)
    graphic.grid_rowconfigure(1, weight = 1)
    # Fim [Elementos Genéricos do Gráfico] // Feito com IA