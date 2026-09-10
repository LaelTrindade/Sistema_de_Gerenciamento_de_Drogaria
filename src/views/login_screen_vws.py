import customtkinter as ctk
from PIL import Image
from config.paths import ASSETS_IMAGES


def login_screen(parent):

    window_width = 800
    window_height = 550
    screen_width = parent.winfo_screenwidth()
    screen_height = parent.winfo_screenheight()

    x = (screen_width - window_width) // 2
    y = (screen_height - window_height) // 2

    parent.geometry(f'{window_width}x{window_height}+{x}+{y}')
    parent.resizable(False, False)

    frame_geral = ctk.CTkFrame(
        master = parent,
        width = 800,
        height = 550,
        corner_radius = 0,
        fg_color = '#b1bdd7'
    )

    frame_geral.grid(row = 0, column = 0, sticky = 'nsew')
    frame_geral.grid_propagate(False)

    frame_1 = ctk.CTkFrame(
        master = frame_geral,
        width = 320,
        height = 400,
        corner_radius = 20,
        fg_color = '#FFFFFF'
    )

    frame_geral.grid_columnconfigure(0, weight = 1)

    frame_1.grid(row = 0, column = 1, sticky = 'nsew', padx = 25, pady = 50)

    frame_2 = ctk.CTkFrame(
        master = frame_geral,
        width = 420,
        height = 530,
        fg_color = 'transparent'
    )

    frame_geral.grid_columnconfigure(1, weight = 1)

    frame_2.grid(row = 0, column = 0, sticky = 'nsw', padx = (10, 0), pady = 10)

    img = ctk.CTkImage(
        light_image = Image.open(ASSETS_IMAGES/'trustmed_image.png'),
        dark_image = Image.open(ASSETS_IMAGES/'trustmed_image.png'),
        size = ((420, 530))
    )

    label_img = ctk.CTkLabel(
        master = frame_2,
        text = '',
        image = img
    )

    label_img.pack(fill = 'both', expand = True)

    icon_img = ctk.CTkImage(
        light_image = Image.open(ASSETS_IMAGES/'doctor_icon.jpeg'),
        dark_image = Image.open(ASSETS_IMAGES/'doctor_icon.jpeg'),
        size = ((100, 100))
    )

    label_icon = ctk.CTkLabel(
        master = frame_1,
        width = 0,
        height = 0,
        text = '',
        image = icon_img
    )

    frame_1.grid_propagate(False)
    frame_1.grid_columnconfigure(0, weight = 1)

    label_icon.grid(row = 0, column = 0, sticky = 'new', pady = (30, 0))

    label_title = ctk.CTkLabel(
        master = frame_1,
        width = 0,
        height = 0,
        font = ('Inter', 22, 'bold'),
        text = 'Bem-vindo de volta!'
    )

    label_title.grid(row = 1, column = 0, sticky = 'new', pady = (15, 0))

    label_subtitle = ctk.CTkLabel(
        master = frame_1,
        width = 0,
        height = 0,
        font = ('DejaVu Sans Condensed', 14),
        text = 'Insira seus dados de acesso'
    )

    label_subtitle.grid(row = 2, column = 0, sticky = 'new', pady = 0)

    label_nome = ctk.CTkLabel(
        master = frame_1,
        width = 0,
        height = 0,
        font = ('DejaVu Sans Condensed', 10),
        text = 'Usuário'
    )

    label_nome.grid(row = 3, column = 0, sticky = 'nw', padx = 35, pady = (25, 0))

    entry_1 = ctk.CTkEntry(
        master = frame_1,
        width = 250,
        height = 20,
        corner_radius = 5,
        border_width = 1,
        font = ('DejaVu Sans Condensed', 10)
    )

    entry_1.grid(row = 4, column = 0, sticky = 'nw', padx = 35, pady = (2, 0))

    label_senha = ctk.CTkLabel(
        master = frame_1,
        width = 0,
        height = 0,
        font = ('DejaVu Sans Condensed', 10),
        text = 'Senha'
    )

    label_senha.grid(row = 5, column = 0, sticky = 'nw', padx = 35, pady = (10, 0))

    entry_2 = ctk.CTkEntry(
        master = frame_1,
        width = 250,
        height = 20,
        corner_radius = 5,
        border_width = 1,
        font = ('DejaVu Sans Condensed', 10),
        show = '•'
    )

    entry_2.grid(row = 6, column = 0, sticky = 'nw', padx = 35, pady = (2, 0))

    label_esqueciSenha = ctk.CTkLabel(
        master = frame_1,
        width = 0,
        height = 0,
        font = ('DejaVu Sans Condensed', 9, 'underline'),
        text = 'Esqueci minha senha',
        cursor = 'hand2'
    )

    label_esqueciSenha.grid(row = 7, column = 0, sticky = 'se', pady = (2, 0), padx = (0, 40))

    button_login = ctk.CTkButton(
        master = frame_1,
        width = 200,
        height = 20,
        corner_radius = 5,
        font = ('Inter', 14, 'bold'),
        fg_color = '#ff3131',
        hover_color = '#D92727',
        text_color = 'white',
        text = 'Login',
        cursor = 'hand2'
    )

    button_login.grid(row = 8, column = 0, sticky = 'n', pady = (25, 0))

    button_cadastro = ctk.CTkButton(
        master = frame_1,
        width = 200,
        height = 20,
        corner_radius = 5,
        font = ('Inter', 14, 'bold'),
        fg_color = '#ff3131',
        hover_color = '#D92727',
        text_color = 'white',
        text = 'Cadastro',
        cursor = 'hand2'
    )

    button_cadastro.grid(row = 9, column = 0, sticky = 'n', pady = 5)

    label_versao = ctk.CTkLabel(
        master = frame_1,
        width = 0,
        height = 0,
        font = ('DejaVu Sans Condensed', 10),
        text = 'v. beta 0.01'
    )

    frame_1.grid_rowconfigure(10, weight = 1)

    label_versao.grid(row = 10, column = 0, sticky = 's', pady = (0, 10))

    return frame_geral