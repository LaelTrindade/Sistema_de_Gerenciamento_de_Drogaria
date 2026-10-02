import customtkinter as ctk
from PIL import Image
from src.config.paths import IMAGES_LOGIN_SCREEN
from src.controllers.auth_controller import validar_login
from src.views.messagebox_vws import exibir_messagebox


def login_screen(parent):

    def clicar_entrar():
    
        from src.views.main_screen_vws import main_screen

        usuario = entry_1.get()
        senha = entry_2.get()

        sucesso, mensagem = validar_login(usuario, senha)

        if sucesso:

            frame_geral.destroy()
            parent.resizable(True, True)

            main_screen(parent)

        else:
            exibir_messagebox(parent, "Erro", mensagem)
                 
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
        corner_radius = 0,
        fg_color = '#EAF3F8'
    )

    frame_geral.grid(row = 0, column = 0, sticky = 'nsew')
    frame_geral.grid_propagate(False)

    frame_geral.grid_columnconfigure(0, weight = 0)
    frame_geral.grid_columnconfigure(1, weight = 1)

    frame_geral.grid_rowconfigure(0, weight = 1)

    side_frame = ctk.CTkFrame(
        master = frame_geral,
        width = 252,
        corner_radius = 0
    )

    side_frame.grid(row = 0, column = 0, sticky = 'nsw')
    side_frame.grid_propagate(False)

    side_image = ctk.CTkLabel(
        master = side_frame,
        width = 0,
        height = 0,
        text = '',
        image = ctk.CTkImage(
            light_image = Image.open(IMAGES_LOGIN_SCREEN/'side_image.png'),
            dark_image = Image.open(IMAGES_LOGIN_SCREEN/'side_image.png'),
            size = ((252, 500))
        )
    )

    side_image.place(x = 0, y = 0, relwidth = 1, relheight = 1)

    login_frame = ctk.CTkFrame(
        master = frame_geral,
        width = 320,
        height = 380,
        border_width = 1,
        corner_radius = 5,
        fg_color = '#FFFFFF',
        border_color = '#D7E4ED'
    )

    login_frame.grid(row = 0, column = 1)
    login_frame.pack_propagate(False)


    title = ctk.CTkLabel(
        master = login_frame,
        width = 0,
        height = 0, 
        text_color = '#1E293B',
        text = 'Bem-vindo de volta!',
        font = ('Montserrat', 21, 'bold')
    )

    title.pack(pady = (35, 0))

    subtitle = ctk.CTkLabel(
        master = login_frame,
        width = 0,
        height = 0,
        font = ('Inter', 13),
        text_color = '#64748B',
        text = 'Insira suas credenciais de acesso'
    )

    subtitle.pack(pady = 0)

    entry_frame_1 = ctk.CTkFrame(
        master = login_frame,
        width = 250,
        height = 35,
        border_width = 1,
        corner_radius = 5,
        fg_color = '#FFFFFF',
        border_color = '#D9E3EC',
    )

    entry_frame_1.pack(padx = 35, pady = (40, 0))
    entry_frame_1.pack_propagate(False)

    user_icon = ctk.CTkLabel(
        master = entry_frame_1,
        width = 0,
        height = 0,
        text = '',
        image = ctk.CTkImage(
            light_image = Image.open(IMAGES_LOGIN_SCREEN/'user_icon.png'),
            dark_image = Image.open(IMAGES_LOGIN_SCREEN/'user_icon.png'),
            size = ((20, 20))
        )
    )

    user_icon.pack(side = 'left', padx = (10, 4))

    entry_1 = ctk.CTkEntry(
        master = entry_frame_1,
        width = 210,
        height = 30,
        border_width = 0,
        font = ('Inter', 12),
        text_color = '#1E293B',
        fg_color = 'transparent',
        placeholder_text = 'login',
        placeholder_text_color = '#94A3B8'
    )

    entry_1.pack(side = 'left', padx = 0)

    entry_frame_2 = ctk.CTkFrame(
        master = login_frame,
        width = 250,
        height = 35,
        border_width = 1,
        corner_radius = 5,
        fg_color = '#FFFFFF',
        border_color = '#D9E3EC',
    )

    entry_frame_2.pack(padx = 35, pady = (10, 0))
    entry_frame_2.pack_propagate(False)

    lock_icon = ctk.CTkLabel(
        master = entry_frame_2,
        width = 0,
        height = 0,
        text = '',
        image = ctk.CTkImage(
            light_image = Image.open(IMAGES_LOGIN_SCREEN/'lock_icon.png'),
            dark_image = Image.open(IMAGES_LOGIN_SCREEN/'lock_icon.png'),
            size = ((20, 18))
        )
    )

    lock_icon.pack(side = 'left', padx = (10, 4))

    entry_2 = ctk.CTkEntry(
        master = entry_frame_2,
        width = 180,
        height = 30,
        show = '•',
        border_width = 0,
        font = ('Inter', 12),
        text_color = '#1E293B',
        fg_color = 'transparent',
        placeholder_text = 'senha',
        placeholder_text_color = '#94A3B8'
    )

    entry_2.pack(side = 'left', padx = 0)

    senha_visivel = None

    def alternar_senha():

        nonlocal senha_visivel
        senha_visivel = not senha_visivel

        if senha_visivel:

            entry_2.configure(show = '')
            eye_button.configure(image = ctk.CTkImage(
                light_image = Image.open(IMAGES_LOGIN_SCREEN/'eye_icon_2.png'),
                dark_image = Image.open(IMAGES_LOGIN_SCREEN/'eye_icon_2.png'),
                size = ((16, 16))
            ))

        else:

            entry_2.configure(show = '•')
            eye_button.configure(image = ctk.CTkImage(
                light_image = Image.open(IMAGES_LOGIN_SCREEN/'eye_icon_1.png'),
                dark_image = Image.open(IMAGES_LOGIN_SCREEN/'eye_icon_1.png'),
                size = ((16, 16))
            ))


    eye_button = ctk.CTkButton(
        master = entry_frame_2,
        width = 40,
        height = 25,
        text = '',
        corner_radius = 5,
        fg_color = 'transparent',
        hover_color = '#FFFFFF',
        image = ctk.CTkImage(
            light_image = Image.open(IMAGES_LOGIN_SCREEN/'eye_icon_1.png'),
            dark_image = Image.open(IMAGES_LOGIN_SCREEN/'eye_icon_1.png'),
            size = ((16, 16))
        ),
        command = alternar_senha
    )

    eye_button.pack(side = 'left', padx = (2, 5))

    forgot_password = ctk.CTkLabel(
        master = login_frame,
        width = 0,
        height = 0,
        cursor = 'hand2',
        compound = 'right',
        text_color = '#064D87',
        text = 'Esqueci minha senha',
        font = ('Inter', 10, 'underline'),
        image = ctk.CTkImage(
            light_image = Image.open(IMAGES_LOGIN_SCREEN/'arrow_icon.png'),
            dark_image = Image.open(IMAGES_LOGIN_SCREEN/'arrow_icon.png'),
            size = ((14, 14))
        )
    )

    forgot_password.pack(side = 'top', anchor = 'e', padx = (0, 36), pady = (5, 0))

    login_button = ctk.CTkButton(
        master = login_frame,
        width = 200,
        height = 40,
        cursor = 'hand2',
        corner_radius = 5,
        compound = 'left',
        text = 'Login',
        font = ('Inter', 14, 'bold'),
        fg_color = '#E84A5A',
        hover_color = '#D94050',
        text_color = '#FFFFFF',
        image = ctk.CTkImage(
            light_image = Image.open(IMAGES_LOGIN_SCREEN/'exit_icon.png'),
            dark_image = Image.open(IMAGES_LOGIN_SCREEN/'exit_icon.png'),
            size = ((20, 20))
        ),
        command = clicar_entrar
    )

    login_button.pack(pady = (25, 0))

    arrows = ctk.CTkLabel(
        master = login_frame,
        width = 0,
        height = 0,
        text = '─'*50,
        font = ('Inter', 8),
        text_color = '#94A3B8'
    )

    arrows.pack(pady = (50, 0))

    security = ctk.CTkLabel(
        master = login_frame,
        width = 0,
        height = 0,
        compound = 'left',
        font = ('Inter', 10),
        text_color = '#163E63',
        text = ' Acesso seguro • Seus dados protegidos',
        image = ctk.CTkImage(
            light_image = Image.open(IMAGES_LOGIN_SCREEN/'shield_icon.png'),
            dark_image = Image.open(IMAGES_LOGIN_SCREEN/'shield_icon.png'),
            size = ((16, 15))
        )
    )

    security.pack(pady = (5, 10))

    return frame_geral