import customtkinter as ctk
from PIL import Image
from src.config.paths import IMAGES_MEDICAMENTOS
from src.services.novo_medicamento_svc import salvar_dados_medicamento


janela_aberta = None

def exibir_novo_medicamento(parent, ao_salvar):

    global janela_aberta

    if janela_aberta is not None and janela_aberta.winfo_exists():

        janela_aberta.focus_force()
        return

    novo_medicamento = ctk.CTkToplevel(
        master = parent
    )

    janela_aberta = novo_medicamento

    novo_medicamento.grid_columnconfigure(0, weight = 1)
    novo_medicamento.grid_rowconfigure(0, weight = 1)

    largura = 650
    altura = 420

    x = ((parent.winfo_x() + (parent.winfo_width()) // 2) - (largura // 2))
    y = ((parent.winfo_y() + (parent.winfo_height()) // 2) - (altura // 2))

    novo_medicamento.overrideredirect(True)
    novo_medicamento.transient(parent.winfo_toplevel())
    novo_medicamento.geometry(f'{largura}x{altura}+{x}+{y}')

    def dar_foco():

        novo_medicamento.focus_force()

    novo_medicamento.after(100, dar_foco)

    fr_transparent = ctk.CTkFrame(
        master = novo_medicamento,
        fg_color = '#073F61',
        border_width = 1,
        corner_radius = 0,
        border_color = '#263746'
    )

    fr_transparent.grid(sticky = 'nsew')

    fr_transparent.grid_columnconfigure(0, weight = 0)
    fr_transparent.grid_columnconfigure(1, weight = 1)
    fr_transparent.grid_rowconfigure(1, weight = 1)

    icon = ctk.CTkLabel(
        master = fr_transparent,
        width = 0,
        height = 0,
        text = '',
        image = ctk.CTkImage(
            light_image = Image.open(IMAGES_MEDICAMENTOS/'pill_icon_2.png'),
            dark_image = Image.open(IMAGES_MEDICAMENTOS/'pill_icon_2.png'),
            size = (44, 44)
        )
    )

    icon.grid(row = 0, column = 0, sticky = 'nw', padx = (20, 0), pady = (20, 0))

    fr_texts = ctk.CTkFrame(
        master = fr_transparent,
        fg_color = 'transparent'
    )

    fr_texts.grid(row = 0, column = 1, sticky = 'nw', padx = (12, 0), pady = (20, 0))

    title = ctk.CTkLabel(
        master = fr_texts,
        width = 0,
        height = 0,
        text_color = '#DCEAF3',
        text = 'Novo Medicamento',
        font = ('Inter', 20, 'bold')
    )

    title.grid(row = 0, column = 0, sticky = 'w')

    subtitle = ctk.CTkLabel(
        master = fr_texts,
        width = 0,
        height = 0,
        font = ('Inter', 14),
        text_color = '#DCEAF3',
        text = 'Preencha os campos abaixo para cadastrar um novo medicamento'
    )

    subtitle.grid(row = 1, column = 0, sticky = 'w')


# Início fr_conteudo
    fr_conteudo = ctk.CTkFrame(
        master = fr_transparent,
        corner_radius = 0,
        fg_color = '#FFFFFF'
    )

    fr_conteudo.grid(row = 1, column = 0, sticky = 'nsew', padx = 1, pady = (20, 1), columnspan = 2)

    fr_conteudo.grid_columnconfigure(0, weight = 1)
    fr_conteudo.grid_columnconfigure(1, weight = 1)

    # Início nome_medicamento
    nome_medicamento = ctk.CTkLabel(
        master = fr_conteudo,
        width = 0,
        height = 0,
        anchor = 'w',
        compound = 'left',
        font = ('Inter', 14),
        text = ' Nome Comercial',
        text_color = '#183E64',
        image = ctk.CTkImage(
            light_image = Image.open(IMAGES_MEDICAMENTOS/'tag_icon.png'),
            dark_image = Image.open(IMAGES_MEDICAMENTOS/'tag_icon.png'),
            size = ((16, 16))
        )
    )

    nome_medicamento.grid(row = 0, column = 0, sticky = 'w', padx = (20, 0), pady = (25, 0))

    frame_nome = ctk.CTkFrame(
        master = fr_conteudo,
        width = 605,
        height = 35,
        border_width = 1,
        corner_radius = 5,
        fg_color = '#FFFFFF',
        border_color = '#D9E3EC'
    )

    frame_nome.grid(row = 1, column = 0, sticky = 'ew', padx = 20, pady = (4, 0), columnspan = 2)
    frame_nome.pack_propagate(False)

    entry_1 = ctk.CTkEntry(
        master = frame_nome,
        border_width = 0,
        font = ('Inter', 14),
        text_color = '#1E293B',
        fg_color = 'transparent',
        placeholder_text = 'Ex.: Dipirona 500mg',
        placeholder_text_color = '#94A3B8'    
    )

    entry_1.pack(fill = 'both', expand = True, padx = 5, pady = 5)
    # Fim nome_medicamento

    # Início ativo
    ativo = ctk.CTkLabel(
        master = fr_conteudo,
        width = 0,
        height = 0,
        anchor = 'w',
        compound = 'left',
        font = ('Inter', 14),
        text = ' Princípio Ativo',
        text_color = '#183E64',
        image = ctk.CTkImage(
            light_image = Image.open(IMAGES_MEDICAMENTOS/'chemistry_icon.png'),
            dark_image = Image.open(IMAGES_MEDICAMENTOS/'chemistry_icon.png'),
            size = ((16, 16))
        )
    )

    ativo.grid(row = 2, column = 0, sticky = 'w', padx = (20, 0), pady = (25, 0))

    frame_ativo = ctk.CTkFrame(
        master = fr_conteudo,
        width = 296,
        height = 35,
        border_width = 1,
        corner_radius = 5,
        fg_color = '#FFFFFF',
        border_color = '#D9E3EC'
    )

    frame_ativo.grid(row = 3, column = 0, sticky = 'w', padx = (20, 0), pady = (4, 0))
    frame_ativo.pack_propagate(False)

    entry_2 = ctk.CTkEntry(
        master = frame_ativo,
        border_width = 0,
        font = ('Inter', 14),
        text_color = '#1E293B',
        fg_color = 'transparent',
        placeholder_text = 'Ex.: Dipirona sódica',
        placeholder_text_color = '#94A3B8'    
    )

    entry_2.pack(fill = 'both', expand = True, padx = 5, pady = 5)
    # Fim ativo

    # Início laboratorio
    laboratorio = ctk.CTkLabel(
        master = fr_conteudo,
        width = 0,
        height = 0,
        anchor = 'w',
        compound = 'left',
        font = ('Inter', 14),
        text = ' Laboratório',
        text_color = '#183E64',
        image = ctk.CTkImage(
            light_image = Image.open(IMAGES_MEDICAMENTOS/'building_icon.png'),
            dark_image = Image.open(IMAGES_MEDICAMENTOS/'building_icon.png'),
            size = ((16, 16))
        )
    )

    laboratorio.grid(row = 2, column = 1, sticky = 'w', padx = (15, 20), pady = (25, 0))

    frame_laboratorio = ctk.CTkFrame(
        master = fr_conteudo,
        width = 296,
        height = 35,
        border_width = 1,
        corner_radius = 5,
        fg_color = '#FFFFFF',
        border_color = '#D9E3EC'
    )

    frame_laboratorio.grid(row = 3, column = 1, sticky = 'w', padx = (15, 20), pady = (4, 0))
    frame_laboratorio.pack_propagate(False)

    entry_3 = ctk.CTkEntry(
        master = frame_laboratorio,
        border_width = 0,
        font = ('Inter', 14),
        text_color = '#1E293B',
        fg_color = 'transparent',
        placeholder_text = 'Ex.: EMS',
        placeholder_text_color = '#94A3B8'    
    )

    entry_3.pack(fill = 'both', expand = True, padx = 5, pady = 5)
    # Fim laboratorio

    # Início categoria
    categoria = ctk.CTkLabel(
        master = fr_conteudo,
        width = 0,
        height = 0,
        anchor = 'w',
        compound = 'left',
        font = ('Inter', 14),
        text = ' Categoria',
        text_color = '#183E64',
        image = ctk.CTkImage(
            light_image = Image.open(IMAGES_MEDICAMENTOS/'category_icon.png'),
            dark_image = Image.open(IMAGES_MEDICAMENTOS/'category_icon.png'),
            size = ((16, 16))
        )
    )

    categoria.grid(row = 4, column = 0, sticky = 'w', padx = (20, 0), pady = (25, 0))

    frame_categoria = ctk.CTkFrame(
        master = fr_conteudo,
        width = 296,
        height = 35,
        border_width = 1,
        corner_radius = 5,
        fg_color = '#FFFFFF',
        border_color = '#D9E3EC'
    )

    frame_categoria.grid(row = 5, column = 0, sticky = 'w', padx = (20, 0), pady = (4, 0))
    frame_categoria.pack_propagate(False)

    option_categorias = [
        'Analgésico / Antitérmico',
        'Anti-inflamatório',
        'Antibiótico',
        'Antialérgico',
        'Vitamina / Suplemento',
        'Outro',
    ]

    option_menu = ctk.CTkOptionMenu(
        master = frame_categoria,
        values = option_categorias,
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

    option_menu.pack(fill = 'both', expand = True, padx = 5, pady = 5)
    # Fim categoria

    # Início valor
    valor = ctk.CTkLabel(
        master = fr_conteudo,
        width = 0,
        height = 0,
        anchor = 'w',
        text = ' Preço',
        compound = 'left',
        font = ('Inter', 14),
        text_color = '#183E64',
        image = ctk.CTkImage(
            light_image = Image.open(IMAGES_MEDICAMENTOS/'cash_icon.png'),
            dark_image = Image.open(IMAGES_MEDICAMENTOS/'cash_icon.png'),
            size = ((18, 16))
        )
    )

    valor.grid(row = 4, column = 1, sticky = 'w', padx = (15, 0), pady = (25, 0))

    frame_valor = ctk.CTkFrame(
        master = fr_conteudo,
        width = 296,
        height = 35,
        border_width = 1,
        corner_radius = 5,
        fg_color = '#FFFFFF',
        border_color = '#D9E3EC'
    )

    frame_valor.grid(row = 5, column = 1, sticky = 'w', padx = (15, 20), pady = (4, 0))
    frame_valor.pack_propagate(False)


    def formatar_preco(event):

        texto = entry_4.get()
        numeros = ''.join(c for c in texto if c.isdigit())[:8]

        if not numeros or int(numeros) == 0:
            entry_4.delete(0, 'end')
            return

        valor = int(numeros) / 100
        novo_texto = f'R$ {valor:,.2f}'.replace(',', 'X').replace('.', ',').replace('X', '.')

        entry_4.delete(0, 'end')
        entry_4.insert(0, novo_texto)


    entry_4 = ctk.CTkEntry(
        master = frame_valor,
        border_width = 0,
        font = ('Inter', 14),
        text_color = '#1E293B',
        fg_color = 'transparent',
        placeholder_text = 'Ex.: 8,50',
        placeholder_text_color = '#94A3B8'    
    )

    entry_4.pack(fill = 'both', expand = True, padx = 5, pady = 5)
    entry_4.bind('<KeyRelease>', formatar_preco)
    # Fim valor

# Fim fr_conteudo

# Início fr_actions
    fr_actions = ctk.CTkFrame(
        master = fr_conteudo,
        corner_radius = 0,
        fg_color = '#E2E6EA'
    )

    fr_actions.grid(row = 6, column = 0, pady = (25, 0), sticky = 'sew', columnspan = 2)
    
    fr_actions.grid_propagate(False)
    fr_actions.grid_columnconfigure(0, weight = 1)


    lb_message = ctk.CTkLabel(
        master = fr_actions,
        width = 0,
        height = 0,
        text = '',
        text_color = '#D93036',
        font = ('Inter', 12, 'bold'),
    )

    lb_message.grid(row = 0, column = 0, sticky = 'w', padx = (20, 0), pady = 12)


    def fechar_toplevel():

        novo_medicamento.destroy()


    cancel_button = ctk.CTkButton(
        master = fr_actions,
        width = 100,
        height = 40,
        anchor = 'w',
        cursor = 'hand2',
        compound = 'left',
        text = 'Cancelar',
        font = ('Inter', 12),
        border_width = 1,
        corner_radius = 5,
        text_color = '#073F61',
        fg_color = 'transparent',
        hover_color = '#D3DCE4',
        border_color = '#073F61',
        image = ctk.CTkImage(
            light_image = Image.open(IMAGES_MEDICAMENTOS/'cross_icon.png'),
            dark_image = Image.open(IMAGES_MEDICAMENTOS/'cross_icon.png'),
            size = ((20, 20))
        ),
        command = fechar_toplevel
    )

    cancel_button.grid(row = 0, column = 1, sticky = 'e', padx = 10, pady = 10)


    def salvar_dados():

        ok, mensagem = salvar_dados_medicamento(
                            entry_1.get(),
                            entry_2.get(),
                            entry_3.get(),
                            option_menu.get(),
                            entry_4.get()
                        )

        if ok:

            ao_salvar()

            lb_message.configure(text = mensagem, text_color = '#20B486')
            lb_message.after(2000, fechar_toplevel)

            save_button.configure(state = 'disabled')

        else:

            lb_message.configure(text = mensagem)
            lb_message.after(5000, lambda: lb_message.configure(text = ''))


    save_button = ctk.CTkButton(
        master = fr_actions,
        width = 166,
        height = 45,
        anchor = 'w',
        cursor = 'hand2',
        compound = 'left',
        font = ('Inter', 12),
        text = 'Salvar medicamento',
        border_width = 1,
        corner_radius = 5,
        text_color = '#DCEAF3',
        fg_color = '#073F61',
        hover_color = '#0B5278',
        border_color = '#245B76',
        image = ctk.CTkImage(
            light_image = Image.open(IMAGES_MEDICAMENTOS/'disk_icon.png'),
            dark_image = Image.open(IMAGES_MEDICAMENTOS/'disk_icon.png'),
            size = ((24, 24))
        ),
        command = salvar_dados
    )

    save_button.grid(row = 0, column = 2, sticky = 'e', padx = (0, 10), pady = 10)