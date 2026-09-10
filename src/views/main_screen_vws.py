import customtkinter as ctk
from views.login_screen_vws import login_screen


def main_screen():

    ctk.set_appearance_mode('Light')

    main_window = ctk.CTk()
    main_window.title('TrustMED')

    login_screen(main_window)


    main_window.mainloop()