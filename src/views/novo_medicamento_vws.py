import json
import os
import customtkinter as ctk
from PIL import Image
from tkinter import messagebox
from src.config.paths import IMAGES_MEDICAMENTOS


janela_aberta = None

def exibir_novo_medicamento(parent):

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
    novo_medicamento.geometry(f'{largura}x{altura}+{x}+{y}')

    def dar_foco():

        novo_medicamento.focus_force()

    novo_medicamento.after(100, dar_foco)

    fr_transparent = ctk.CTkFrame(
        master = novo_medicamento,
        fg_color = '#073F61',
        border_width = 1,
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
        width = 296,
        height = 35,
        border_width = 1,
        corner_radius = 5,
        fg_color = '#FFFFFF',
        border_color = '#D9E3EC'
    )

    frame_nome.grid(row = 1, column = 0, sticky = 'w', padx = (20, 0), pady = (4, 0))
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

    ativo.grid(row = 0, column = 1, sticky = 'w', padx = (15, 20), pady = (25, 0))

    frame_ativo = ctk.CTkFrame(
        master = fr_conteudo,
        width = 296,
        height = 35,
        border_width = 1,
        corner_radius = 5,
        fg_color = '#FFFFFF',
        border_color = '#D9E3EC'
    )

    frame_ativo.grid(row = 1, column = 1, sticky = 'w', padx = (15, 20), pady = (4, 0))
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

    laboratorio.grid(row = 2, column = 0, sticky = 'w', padx = (20, 0), pady = (25, 0))

    frame_laboratorio = ctk.CTkFrame(
        master = fr_conteudo,
        width = 296,
        height = 35,
        border_width = 1,
        corner_radius = 5,
        fg_color = '#FFFFFF',
        border_color = '#D9E3EC'
    )

    frame_laboratorio.grid(row = 3, column = 0, sticky = 'w', padx = (20, 0), pady = (4, 0))
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

    categoria.grid(row = 2, column = 1, sticky = 'w', padx = (15, 20), pady = (25, 0))

    frame_categoria = ctk.CTkFrame(
        master = fr_conteudo,
        width = 296,
        height = 35,
        border_width = 1,
        corner_radius = 5,
        fg_color = '#FFFFFF',
        border_color = '#D9E3EC'
    )

    frame_categoria.grid(row = 3, column = 1, sticky = 'w', padx = (15, 20), pady = (4, 0))
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

    # Início lote
    fr_transparent_2 = ctk.CTkFrame(
        master = fr_conteudo,
        fg_color = 'transparent'
    )

    fr_transparent_2.grid(row = 4, column = 0, sticky = 'ew', padx = 20, pady = (25, 0), columnspan = 2)

    fr_transparent_2.grid_columnconfigure(0, weight = 0)
    
    lote = ctk.CTkLabel(
        master = fr_transparent_2,
        width = 0,
        height = 0,
        anchor = 'w',
        text = ' Lote',
        compound = 'left',
        font = ('Inter', 14),
        text_color = '#183E64',
        image = ctk.CTkImage(
            light_image = Image.open(IMAGES_MEDICAMENTOS/'barcode_icon.png'),
            dark_image = Image.open(IMAGES_MEDICAMENTOS/'barcode_icon.png'),
            size = ((16, 16))
        )
    )

    lote.grid(row = 0, column = 0, sticky = 'w')

    frame_lote = ctk.CTkFrame(
        master = fr_transparent_2,
        width = 192,
        height = 35,
        border_width = 1,
        corner_radius = 5,
        fg_color = '#FFFFFF',
        border_color = '#D9E3EC'
    )

    frame_lote.grid(row = 1, column = 0, sticky = 'w', pady = (4, 0))
    frame_lote.pack_propagate(False)

    entry_4 = ctk.CTkEntry(
        master = frame_lote,
        border_width = 0,
        font = ('Inter', 14),
        text_color = '#1E293B',
        fg_color = 'transparent',
        placeholder_text = 'Ex.: L240815',
        placeholder_text_color = '#94A3B8'    
    )

    entry_4.pack(fill = 'both', expand = True, padx = 5, pady = 5)

    validade = ctk.CTkLabel(
        master = fr_transparent_2,
        width = 0,
        height = 0,
        anchor = 'w',
        text = ' Validade',
        compound = 'left',
        font = ('Inter', 14),
        text_color = '#183E64',
        image = ctk.CTkImage(
            light_image = Image.open(IMAGES_MEDICAMENTOS/'calendar_icon.png'),
            dark_image = Image.open(IMAGES_MEDICAMENTOS/'calendar_icon.png'),
            size = ((16, 16))
        )
    )

    validade.grid(row = 0, column = 1, sticky = 'w', padx = 15)

    frame_validade = ctk.CTkFrame(
        master = fr_transparent_2,
        width = 192,
        height = 35,
        border_width = 1,
        corner_radius = 5,
        fg_color = '#FFFFFF',
        border_color = '#D9E3EC'
    )

    frame_validade.grid(row = 1, column = 1, sticky = 'w', padx = 15, pady = (4, 0))
    frame_validade.pack_propagate(False)

    def formatar_validade(event):

        texto = entry_5.get()
        numeros = ''.join(c for c in texto if c.isdigit())[:8]

        if len(numeros) > 4:
            novo_texto = f'{numeros[:2]}/{numeros[2:4]}/{numeros[4:]}'

        elif len(numeros) > 2:
            novo_texto = f'{numeros[:2]}/{numeros[2:]}'

        else:
            novo_texto = numeros

        entry_5.delete(0, 'end')
        entry_5.insert(0, novo_texto)


    entry_5 = ctk.CTkEntry(
        master = frame_validade,
        border_width = 0,
        font = ('Inter', 14),
        text_color = '#1E293B',
        fg_color = 'transparent',
        placeholder_text = 'Ex.: DD/MM/AAAA',
        placeholder_text_color = '#94A3B8'    
    )

    entry_5.pack(fill = 'both', expand = True, padx = 5, pady = 5)
    entry_5.bind('<KeyRelease>', formatar_validade)

    valor = ctk.CTkLabel(
        master = fr_transparent_2,
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

    valor.grid(row = 0, column = 2, sticky = 'w')

    frame_valor = ctk.CTkFrame(
        master = fr_transparent_2,
        width = 192,
        height = 35,
        border_width = 1,
        corner_radius = 5,
        fg_color = '#FFFFFF',
        border_color = '#D9E3EC'
    )

    frame_valor.grid(row = 1, column = 2, sticky = 'w', pady = (4, 0))
    frame_valor.pack_propagate(False)


    def formatar_preco(event):

        texto = entry_6.get()
        numeros = ''.join(c for c in texto if c.isdigit())[:8]

        if not numeros or int(numeros) == 0:
            entry_6.delete(0, 'end')
            return

        valor = int(numeros) / 100
        novo_texto = f'R$ {valor:,.2f}'.replace(',', 'X').replace('.', ',').replace('X', '.')

        entry_6.delete(0, 'end')
        entry_6.insert(0, novo_texto)


    entry_6 = ctk.CTkEntry(
        master = frame_valor,
        border_width = 0,
        font = ('Inter', 14),
        text_color = '#1E293B',
        fg_color = 'transparent',
        placeholder_text = 'Ex.: 8,50',
        placeholder_text_color = '#94A3B8'    
    )

    entry_6.pack(fill = 'both', expand = True, padx = 5, pady = 5)
    entry_6.bind('<KeyRelease>', formatar_preco)

# Fim fr_conteudo

# Início fr_actions
    fr_actions = ctk.CTkFrame(
        master = fr_conteudo,
        corner_radius = 0,
        fg_color = '#E2E6EA'
    )

    fr_actions.grid(row = 5, column = 0, pady = (25, 0), sticky = 'sew', columnspan = 2)
    
    fr_actions.grid_propagate(False)
    fr_actions.grid_columnconfigure(0, weight = 1)


    def fechar_toplevel():

        novo_medicamento.destroy()

    def salvar_dados_medicamento():
        
        nome = entry_1.get().strip()
        principio = entry_2.get().strip()
        laboratorio = entry_3.get().strip()
        categoria = option_menu.get().strip()
        lote = entry_4.get().strip()
        validade = entry_5.get().strip()
        preco = entry_6.get().strip()

        if not nome or not principio or not laboratorio or not lote or not validade or not preco:

            lbl_mensagem.configure(text="Preencha todos os campos.", text_color="#FF4C4C")
            return  

        novo_remedio = {
            "nome_comercial": nome,
            "principio_ativo": principio,
            "laboratorio": laboratorio,
            "categoria": categoria,
            "lote": lote,
            "validade": validade,
            "preco": preco
        }

        arquivo_banco = "medicamento.json"
        lista_de_medicamentos = []

        if os.path.exists(arquivo_banco):
            try:
                with open(arquivo_banco, "r", encoding="utf-8") as arquivo:
                    conteudo_atual = arquivo.read()
                    if conteudo_atual.strip():
                        lista_de_medicamentos = json.loads(conteudo_atual)
                    
                        if not isinstance(lista_de_medicamentos, list):
                            lista_de_medicamentos = [lista_de_medicamentos]
            except Exception:
                lista_de_medicamentos = []

        lista_de_medicamentos.append(novo_remedio)

        with open(arquivo_banco, "w", encoding="utf-8") as arquivo:
            json.dump(lista_de_medicamentos, arquivo, ensure_ascii=False, indent=4)
        
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

    cancel_button.grid(row = 1, column = 0, sticky = 'e', padx = 10, pady = 10)

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
        command = salvar_dados_medicamento
    )

    save_button.grid(row = 1, column = 1, sticky = 'e', padx = (0, 10), pady = 10)

    lbl_mensagem = ctk.CTkLabel(
        master = fr_actions,
        text = "",
        font = ('Inter', 12, 'bold')
    )
    lbl_mensagem.grid(row = 1, column = 0, columnspan = 2, pady = (5, 0))