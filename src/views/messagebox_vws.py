import customtkinter as ctk
from PIL import Image
from src.config.paths import IMAGES_MESSAGEBOX


MODO_SUCESSO = 1
MODO_ALERTA = 2
MODO_ERRO = 3
MODO_OUTROS = 4
MODO_BOOLEANO = 5

janela_aberta = None

def exibir_messagebox(parent, modo, mensagem, ao_confirmar = None):

    global janela_aberta

    if janela_aberta is not None and janela_aberta.winfo_exists():

        janela_aberta.focus_force()
        return


    messagebox = ctk.CTkToplevel(parent)
    janela_aberta = messagebox

    largura_messagebox = 360
    altura_messagebox = 190

    x = ((parent.winfo_x() + (parent.winfo_width()) // 2) - (largura_messagebox // 2))
    y = ((parent.winfo_y() + (parent.winfo_height()) // 2) - (altura_messagebox // 2))

    messagebox.overrideredirect(True)
    messagebox.transient(parent.winfo_toplevel())
    messagebox.geometry(f'{largura_messagebox}x{altura_messagebox}+{x}+{y}')

    messagebox.grid_columnconfigure(0, weight = 1)
    messagebox.grid_rowconfigure(0, weight = 1)

    fr_transparent = ctk.CTkFrame(
        master = messagebox,
        corner_radius = 0,
        border_width = 2,
        border_color = '#DCE6EE',
        fg_color = 	'#FFFFFF'
    )    

    fr_transparent.grid(row = 0, column = 0, sticky = 'nsew')
    fr_transparent.pack_propagate(False)

    label_title = ctk.CTkLabel(
        master = fr_transparent,
        width = 0,
        height = 0,
        anchor = 'w',
        compound = 'left',
        font = ('Inter', 16, 'bold'),
        text = ''
    )

    label_title.pack(side = 'top', anchor = 'center', pady = (20, 0))

    label_message = ctk.CTkLabel(
        master = fr_transparent,
        width = 0,
        height = 0,
        text = mensagem,
        wraplength = 320,
        font = ('Inter', 14)
    )

    label_message.pack(anchor = 'center', expand = True, pady = 5)


    def fechar_messagebox():
            
        global janela_aberta

        janela_aberta = None
        messagebox.destroy()


    button = ctk.CTkButton(
        master = fr_transparent,
        width = 75,
        height = 30,
        text = 'Ok',
        cursor = 'hand2',
        corner_radius = 5,
        text_color = '#FFFFFF',
        font = ('Inter', 15, 'bold'),
        command = fechar_messagebox
    )

    button.pack(anchor = 'center', pady = (0, 20))

    if modo == MODO_SUCESSO:

        fr_transparent.configure(fg_color = '#E8F7F1', border_color = '#B8E8D5')

        label_title.configure(text = ' Sucesso!', text_color = '#20B486', image = ctk.CTkImage(
            light_image = Image.open(IMAGES_MESSAGEBOX/'sucess_icon.png'),
            dark_image = Image.open(IMAGES_MESSAGEBOX/'sucess_icon.png'),
            size = ((16, 16))
        ))

        button.configure(fg_color = '#20B486', hover_color = '#199B73')

    if modo == MODO_ALERTA:

        fr_transparent.configure(fg_color = '#FFF7E6', border_color = '#F0D99F')

        label_title.configure(text = ' Alerta!', text_color = '#D99A18', image = ctk.CTkImage(
            light_image = Image.open(IMAGES_MESSAGEBOX/'warning_icon.png'),
            dark_image = Image.open(IMAGES_MESSAGEBOX/'warning_icon.png'),
            size = ((16, 16))
        ))

        button.configure(fg_color = '#D99A18', hover_color = '#B98212')

    if modo == MODO_ERRO:

        fr_transparent.configure(fg_color = '#FFF1F1', border_color = '#F3B8BA')

        label_title.configure(text = ' Erro!', text_color = '#E74C4C', image = ctk.CTkImage(
            light_image = Image.open(IMAGES_MESSAGEBOX/'error_icon.png'),
            dark_image = Image.open(IMAGES_MESSAGEBOX/'error_icon.png'),
            size = ((16, 16))
        ))

        button.configure(fg_color = '#E74C4C', hover_color = '#CC3D3D')

    if modo == MODO_OUTROS:

        fr_transparent.configure(fg_color = '#E8F3FA', border_color = '#B8DCEC')

        label_title.configure(text = ' Informação!', text_color = '#1C6EA4', image = ctk.CTkImage(
            light_image = Image.open(IMAGES_MESSAGEBOX/'info_icon.png'),
            dark_image = Image.open(IMAGES_MESSAGEBOX/'info_icon.png'),
            size = ((16, 16))
        ))

        button.configure(fg_color = '#1C6EA4', hover_color = '#155A88')

    if modo == MODO_BOOLEANO:

        fr_transparent.configure(fg_color = '#E8F3FA', border_color = '#B8DCEC')

        label_title.configure(text = ' Informação!', text_color = '#1C6EA4', image = ctk.CTkImage(
            light_image = Image.open(IMAGES_MESSAGEBOX/'info_icon.png'),
            dark_image = Image.open(IMAGES_MESSAGEBOX/'info_icon.png'),
            size = ((16, 16))
        ))


        def confirmar():

            fechar_messagebox()

            if ao_confirmar:

                ao_confirmar()


        button.configure(text = 'Sim', fg_color = '#1C6EA4', hover_color = '#155A88', command = confirmar)
        button.pack_configure(side = 'left', anchor = 's', padx = (75, 0))

        button_2 = ctk.CTkButton(
            master = fr_transparent,
            width = 75,
            height = 30,
            text = 'Não',
            cursor = 'hand2',
            corner_radius = 5,
            text_color = '#FFFFFF',
            font = ('Inter', 15, 'bold'),
            command = fechar_messagebox
        )

        button_2.configure(text = 'Não', fg_color = '#1C6EA4', hover_color = '#155A88')
        button_2.pack(side = 'right', anchor = 's', padx = (0, 75), pady = (0, 20))