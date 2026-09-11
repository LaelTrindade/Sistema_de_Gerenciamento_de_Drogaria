import customtkinter as ctk
from PIL import Image
from config.paths import ASSETS_IMAGES


def login_screen(parent):

    window_width = 720
    window_height = 500
    screen_width = parent.winfo_screenwidth()
    screen_height = parent.winfo_screenheight()

    x = (screen_width - window_width) // 2
    y = (screen_height - window_height) // 2

    parent.geometry(f'{window_width}x{window_height}+{x}+{y}')
    parent.resizable(False, False)

    frame_geral = ctk.CTkFrame(
        master = parent,
        width = 720,
        height = 500,
        corner_radius = 0
    )

    frame_geral.grid(row = 0, column = 0, sticky = 'nsew')
    frame_geral.grid_propagate(False)

    bg_image = ctk.CTkImage(
        light_image = Image.open(ASSETS_IMAGES/'login_page_template.png'),
        dark_image = Image.open(ASSETS_IMAGES/'login_page_template.png'),
        size = ((720, 500))
    )

    label_bgimage = ctk.CTkLabel(
        master = frame_geral,
        width = 0,
        height = 0,
        text = '',
        image = bg_image
    )

    label_bgimage.place(x = 0, y = 0, relwidth = 1, relheight = 1)

    login_frame = ctk.CTkFrame(
        master = frame_geral,
        width = 360,
        height = 420,
        corner_radius = 10,
        fg_color = '#FFFFFF',
        bg_color = '#05385b'
    )

    frame_geral.grid_columnconfigure(0, weight = 1)
    frame_geral.grid_rowconfigure(0, weight = 1)

    login_frame.grid(row = 0, column = 0, sticky = 'nsw', padx = 30, pady = 40)

    logo_img = ctk.CTkImage(
        light_image = Image.open(ASSETS_IMAGES/'trustmed_icon_logo.png'),
        dark_image = Image.open(ASSETS_IMAGES/'trustmed_icon_logo.png'),
        size = ((140, 20))
    )

    label_logo = ctk.CTkLabel(
        master = login_frame,
        width = 0,
        height = 0,
        text = '',
        image = logo_img
    )

    login_frame.pack_propagate(False)
    label_logo.pack(pady = (35, 0))

    label_title = ctk.CTkLabel(
        master = login_frame,
        width = 0,
        height = 0,
        font = ('Montserrat', 21, 'bold'),
        text = 'Bem-vindo de volta!'
    )

    label_title.pack(pady = (20, 0))

    label_subtitle = ctk.CTkLabel(
        master = login_frame,
        width = 0,
        height = 0,
        font = ('Montserrat', 14),
        text = 'Insira seus dados de acesso'
    )

    label_subtitle.pack(pady = 0)

    usericon_img = ctk.CTkImage(
        light_image = Image.open(ASSETS_IMAGES/'user_icon.png'),
        dark_image = Image.open(ASSETS_IMAGES/'user_icon.png'),
        size = ((12, 12))
    )

    label_usuario = ctk.CTkLabel(
        master = login_frame,
        width = 0,
        height = 0,
        image = usericon_img,
        compound = 'left',
        font = ('Inter', 12),
        text = ' Usuário'
    )

    label_usuario.pack(padx = 52, pady = (35, 0), side = 'top', anchor = 'w')

    entry_1 = ctk.CTkEntry(
        master = login_frame,
        width = 300,
        height = 25,
        corner_radius = 5,
        border_width = 1,
        font = ('Inter', 10)
    )

    entry_1.pack(padx = 50, pady = (2, 0), side = 'top', anchor = 'w')

    lockicon_img = ctk.CTkImage(
        light_image = Image.open(ASSETS_IMAGES/'lock_icon.png'),
        dark_image = Image.open(ASSETS_IMAGES/'lock_icon.png'),
        size = ((12, 12))
    )

    label_senha = ctk.CTkLabel(
        master = login_frame,
        width = 0,
        height = 0,
        image = lockicon_img,
        compound = 'left',
        font = ('Inter', 12),
        text = ' Senha'
    )

    label_senha.pack(padx = 52, pady = (10, 0), side = 'top', anchor = 'w')

    entry_2 = ctk.CTkEntry(
        master = login_frame,
        width = 300,
        height = 25,
        corner_radius = 5,
        border_width = 1,
        font = ('Inter', 10),
        show = '•'
    )

    entry_2.pack(padx = 50, pady = (2, 0), side = 'top', anchor = 'w')

    label_esqueci_minha_senha = ctk.CTkLabel(
        master = login_frame,
        width = 0,
        height = 0,
        font = ('Inter', 8, 'underline'),
        text = 'Esqueci minha senha',
        cursor = 'hand2'
    )

    label_esqueci_minha_senha.pack(padx = 55, pady = (2, 0), side = 'top', anchor = 'e')

    button_login = ctk.CTkButton(
        master = login_frame,
        width = 200,
        height = 25,
        corner_radius = 5,
        text = 'Login',
        text_color = '#FFFFFF',
        font = ('Montserrat', 12, 'bold'),
        fg_color = '#FF3131',
        hover_color = '#D92828',
        cursor = 'hand2'
    )

    button_login.pack(pady = (30, 0))

    label_divisoria = ctk.CTkLabel(
        master = login_frame,
        width = 0,
        height = 0,
        font = ('Inter', 10),
        text = '─'*16+'  admin  '+'─'*16,
        text_color = '#666666'
    )

    label_divisoria.pack(pady = (15, 0))

    button_cadastro = ctk.CTkButton(
        master = login_frame,
        width = 200,
        height = 25,
        corner_radius = 5,
        text = 'Cadastrar Usuário',
        text_color = '#FFFFFF',
        font = ('Montserrat', 12, 'bold'),
        fg_color = '#FF3131',
        hover_color = '#D92828',
        cursor = 'hand2'
    )

    button_cadastro.pack(pady = (15, 0))


    return frame_geral