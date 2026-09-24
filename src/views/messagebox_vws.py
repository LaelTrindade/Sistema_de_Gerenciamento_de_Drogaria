import customtkinter as ctk
from PIL import Image
from src.config.paths import ASSETS_IMAGES


messagebox = None

def exibir_messagebox(parent, title, text):

    global messagebox

    if messagebox is not None and messagebox.winfo_exists():

        return

    messagebox = ctk.CTkToplevel(parent)
    messagebox.title(title)

    parent_x = parent.winfo_x()
    parent_y = parent.winfo_y()
    parent_width = parent.winfo_width()
    parent_height = parent.winfo_height()

    messagebox_width = 365
    messagebox_height = 160
    x = parent_x + (parent_width - messagebox_width) // 2
    y = parent_y + (parent_height - messagebox_height) // 2

    messagebox.geometry(f'{messagebox_width}x{messagebox_height}+{x}+{y}')
    messagebox.configure(fg_color = '#F5F5F5')
    messagebox.resizable(False, False)

    icon_img = ctk.CTkImage(
        light_image = Image.open(ASSETS_IMAGES/'icon_logo.png'),
        dark_image = Image.open(ASSETS_IMAGES/'icon_logo.png'),
        size = ((38, 38))
    )

    label_text_and_icon = ctk.CTkLabel(
        master = messagebox,
        width = 0,
        height = 0,
        padx = 10,
        text = text,
        image = icon_img,
        wraplength = 280,
        compound = 'left',
        anchor = 'center',
        font = ('Montserrat', 18, 'bold')
    )

    messagebox.grid_propagate(False)
    messagebox.grid_columnconfigure(0, weight = 1)
    messagebox.grid_rowconfigure(0, weight = 0)

    label_text_and_icon.grid(row = 0, column = 0, sticky = 'new', pady = (40, 0))

    def fechar_messagebox():

        messagebox.after(500, messagebox.destroy)

    button_ok = ctk.CTkButton(
        master = messagebox,
        width = 100,
        height = 25,
        corner_radius = 5,
        text = 'Ok',
        cursor = 'hand2',
        text_color = 'white',
        fg_color = '#FF3131',
        hover_color = '#D92828',
        font = ('Montserrat', 12, 'bold'),
        command = fechar_messagebox
    )

    button_ok.grid(row = 1, column = 0, sticky = 'n', pady = (30, 0))