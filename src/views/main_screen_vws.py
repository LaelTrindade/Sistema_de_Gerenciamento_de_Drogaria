import platform
import customtkinter as ctk
from PIL import Image
from src.config.paths import IMAGES_MAIN_SCREEN
from src.views.login_screen_vws import login_screen
from src.views.dashboard_vws import exibir_dashboard
from src.services.clock_service import obter_data_hora



def iniciar_app():

    ctk.set_appearance_mode('Light')

    main_window = ctk.CTk()
    main_window.title('TrustMED+')

    frame_login = login_screen(main_window)

    main_window.mainloop()


def main_screen(parent):

    parent.update_idletasks()

    if platform.system() == 'Windows':

        parent.state('zoomed')

    else:

        parent.after(10, lambda: parent.attributes('-zoomed', True))


    parent.grid_columnconfigure(0, weight = 0)
    parent.grid_columnconfigure(1, weight = 1)

    parent.grid_rowconfigure(0, weight = 0)
    parent.grid_rowconfigure(1, weight = 1)


    cor_normal = 'transparent'
    cor_selecionada = '#0B527D'

    tela_atual = None

    def selecionar_button(nome_tela):

        nonlocal tela_atual

        if nome_tela == tela_atual:

            return
        

        for widget in fr_transparent.winfo_children():
            
            widget.destroy()

        for key, button in sidebar_buttons.items():
            cor = cor_selecionada if key == nome_tela else cor_normal
            button.configure(fg_color = cor)

            if nome_tela == 'dashboard':

                exibir_dashboard(fr_transparent)


        tela_atual = nome_tela

# Início [Topbar].

    topbar = ctk.CTkFrame(
        master = parent,
        height = 56,
        border_width = 1,
        corner_radius = 0,
        fg_color = '#FFFFFF',
        border_color = '#E2EAF1'
    )

    topbar.grid(row = 0, column = 0, sticky = 'new', columnspan = 2)

    topbar.grid_rowconfigure(0, weight = 1)

    topbar.grid_columnconfigure(0, weight = 1)
    topbar.grid_columnconfigure(1, weight = 0)
    topbar.grid_columnconfigure(2, weight = 0)
    topbar.grid_columnconfigure(3, weight = 0)

    topbar.grid_propagate(False)

    def atualizar_relogio():

        data, hora = obter_data_hora()

        calendar.configure(text = f'    {data}\n    {hora}')
        calendar.after(1000, atualizar_relogio)


    logo_icon = ctk.CTkLabel(
        master = topbar,
        width = 0,
        height = 0,
        text = '',
        image = ctk.CTkImage(
            light_image = Image.open(IMAGES_MAIN_SCREEN/'trustmed_logo.png'),
            dark_image = Image.open(IMAGES_MAIN_SCREEN/'trustmed_logo.png'),
            size = ((150, 29))
        )
    )

    logo_icon.grid(row = 0, column = 0, sticky = 'w', padx = 20, pady = 10)

    calendar = ctk.CTkLabel(
        master = topbar,
        width = 0,
        height = 0,
        anchor = 'w',
        compound = 'left',
        justify = 'left',
        font = ('Inter', 10, 'bold'),
        text = '    22 de Setembro de 2026\n    14:25',
        image = ctk.CTkImage(
            light_image = Image.open(IMAGES_MAIN_SCREEN/'calendar_icon.png'),
            dark_image = Image.open(IMAGES_MAIN_SCREEN/'calendar_icon.png'),
            size = ((28, 28))
        )
    )

    calendar.grid(row = 0, column = 1, sticky = 'e', padx = 15, pady = 10)

    vertical_line = ctk.CTkFrame(
        master = topbar,
        width = 1,
        height = 42,
        corner_radius = 0,
        border_width = 2,
        border_color = 'black',
        fg_color = 'black'
    )

    vertical_line.grid(row = 0, column = 2, sticky = 'e', pady = 5)

    user_icon = ctk.CTkLabel(
        master = topbar,
        width = 5,
        height = 5,
        compound = 'left',
        font = ('Inter', 14),
        text = '  Admininstrador',
        image = ctk.CTkImage(
            light_image = Image.open(IMAGES_MAIN_SCREEN/'user_icon.png'),
            dark_image = Image.open(IMAGES_MAIN_SCREEN/'user_icon.png'),
            size = ((36, 36))
        )
    )

    user_icon.grid(row = 0, column = 3, sticky = 'e', padx = (10, 25), pady = 10)

# Fim [Topbar].


# Início [Sidebar].

    sidebar = ctk.CTkFrame(
        master = parent,
        width = 220,
        corner_radius = 0,
        fg_color = '#073F61'
    )

    sidebar.grid(row = 1, column = 0, sticky = 'nsw')

    sidebar.grid_columnconfigure(0, weight = 1)
    sidebar.grid_rowconfigure(6, weight = 1)

    sidebar.grid_propagate(False)

    dashboard = ctk.CTkButton(
        master = sidebar,
        width = 120,
        height = 50,
        anchor = 'w',
        cursor = 'hand2',
        corner_radius = 5,
        font = ('Inter', 14, 'bold'),
        text = '    Dashboard',
        text_color = '#DCEAF3',
        fg_color = 'transparent',
        hover_color = '#0B527D',
        compound = 'left',
        image = ctk.CTkImage(
            light_image = Image.open(IMAGES_MAIN_SCREEN/'dashboard_icon.png'),
            dark_image = Image.open(IMAGES_MAIN_SCREEN/'dashboard_icon.png'),
            size = ((24, 24))
        ),
        command = lambda: selecionar_button('dashboard')
    )

    dashboard.grid(row = 0, column = 0, sticky = 'new', padx = 10, pady = (10, 0))

    medications = ctk.CTkButton(
        master = sidebar,
        width = 120,
        height = 50,
        anchor = 'w',
        cursor = 'hand2',
        corner_radius = 5,
        font = ('Inter', 14, 'bold'),
        text = '    Medicamentos',
        text_color = '#DCEAF3',
        fg_color = 'transparent',
        hover_color = '#0B527D',
        compound = 'left',
        image = ctk.CTkImage(
            light_image = Image.open(IMAGES_MAIN_SCREEN/'medication_icon.png'),
            dark_image = Image.open(IMAGES_MAIN_SCREEN/'medication_icon.png'),
            size = ((24, 24))
        ),
        command = lambda: selecionar_button('medicamentos')
    )

    medications.grid(row = 1, column = 0, sticky = 'ew', padx = 10, pady = (15, 0))

    stock = ctk.CTkButton(
        master = sidebar,
        width = 120,
        height = 50,
        anchor = 'w',
        cursor = 'hand2',
        corner_radius = 5,
        font = ('Inter', 14, 'bold'),
        text = '    Estoque',
        text_color = '#DCEAF3',
        fg_color = 'transparent',
        hover_color = '#0B527D',
        compound = 'left',
        image = ctk.CTkImage(
            light_image = Image.open(IMAGES_MAIN_SCREEN/'box_icon.png'),
            dark_image = Image.open(IMAGES_MAIN_SCREEN/'box_icon.png'),
            size = ((24, 24))
        ),
        command = lambda: selecionar_button('estoque')
    )

    stock.grid(row = 2, column = 0, sticky = 'ew', padx = 10, pady = (15, 0))

    sales = ctk.CTkButton(
        master = sidebar,
        width = 120,
        height = 50,
        anchor = 'w',
        cursor = 'hand2',
        corner_radius = 5,
        font = ('Inter', 14, 'bold'),
        text = '    Vendas',
        text_color = '#DCEAF3',
        fg_color = 'transparent',
        hover_color = '#0B527D',
        compound = 'left',
        image = ctk.CTkImage(
            light_image = Image.open(IMAGES_MAIN_SCREEN/'sales_icon.png'),
            dark_image = Image.open(IMAGES_MAIN_SCREEN/'sales_icon.png'),
            size = ((24, 24))
        ),
        command = lambda: selecionar_button('vendas')
    )

    sales.grid(row = 3, column = 0, sticky = 'ew', padx = 10, pady = (15, 0))

    users = ctk.CTkButton(
        master = sidebar,
        width = 120,
        height = 50,
        anchor = 'w',
        cursor = 'hand2',
        corner_radius = 5,
        font = ('Inter', 14, 'bold'),
        text = '    Funcionários',
        text_color = '#DCEAF3',
        fg_color = 'transparent',
        hover_color = '#0B527D',
        compound = 'left',
        image = ctk.CTkImage(
            light_image = Image.open(IMAGES_MAIN_SCREEN/'users_icon.png'),
            dark_image = Image.open(IMAGES_MAIN_SCREEN/'users_icon.png'),
            size = ((24, 24))
        ),
        command = lambda: selecionar_button('funcionarios')
    )

    users.grid(row = 4, column = 0, sticky = 'ew', padx = 10, pady = (15, 0))

    reports = ctk.CTkButton(
        master = sidebar,
        width = 120,
        height = 50,
        anchor = 'w',
        cursor = 'hand2',
        corner_radius = 5,
        font = ('Inter', 14, 'bold'),
        text = '    Relatórios',
        text_color = '#DCEAF3',
        fg_color = 'transparent',
        hover_color = '#0B527D',
        compound = 'left',
        image = ctk.CTkImage(
            light_image = Image.open(IMAGES_MAIN_SCREEN/'reports_icon.png'),
            dark_image = Image.open(IMAGES_MAIN_SCREEN/'reports_icon.png'),
            size = ((24, 24))
        ),
        command = lambda: selecionar_button('relatorios')
    )

    reports.grid(row = 5, column = 0, sticky = 'ew', padx = 10, pady = (15, 0))

    exit = ctk.CTkButton(
        master = sidebar,
        width = 120,
        height = 50,
        anchor = 'w',
        cursor = 'hand2',
        corner_radius = 5,
        font = ('Inter', 12),
        text = '    Sair',
        text_color = '#DCEAF3',
        fg_color = 'transparent',
        hover_color = '#0B527D',
        compound = 'left',
        image = ctk.CTkImage(
            light_image = Image.open(IMAGES_MAIN_SCREEN/'exit_icon.png'),
            dark_image = Image.open(IMAGES_MAIN_SCREEN/'exit_icon.png'),
            size = ((22, 22))
        )
    )

    exit.grid(row = 7, column = 0, padx = 10, sticky = 'ew', pady = 15)

# Fim [Sidebar].


# Início [Frame "Invisível"].

    fr_transparent = ctk.CTkFrame(
        master = parent,
        corner_radius = 0,
        fg_color = '#F5F8FC'
    )

    fr_transparent.grid(row = 1, column = 1, sticky = 'nsew')

# Fim [Frame "Invisível"].

    # Dicionário para a função selecionar_button
    sidebar_buttons = {
        'dashboard':    dashboard,
        'medicamentos': medications,
        'estoque':      stock,
        'vendas':       sales,
        'funcionarios': users,
        'relatorios':   reports,
    }

    atualizar_relogio()



if __name__ == '__main__':

    main_screen()