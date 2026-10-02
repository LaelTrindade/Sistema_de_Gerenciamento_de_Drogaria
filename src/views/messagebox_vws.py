import customtkinter as ctk


def exibir_messagebox(parent, titulo, mensagem):

    largura_alerta = 350
    altura_alerta = 160

    alerta = ctk.CTkToplevel(parent)

    # Mantém a janela invisível durante a construção
    alerta.withdraw()

    alerta.overrideredirect(True)
    alerta.transient(parent)

    # Calcula a posição central em relação ao parent
    parent.update_idletasks()

    x = (
        parent.winfo_x()
        + (parent.winfo_width() // 2)
        - (largura_alerta // 2)
    )

    y = (
        parent.winfo_y()
        + (parent.winfo_height() // 2)
        - (altura_alerta // 2)
    )

    alerta.geometry(
        f"{largura_alerta}x{altura_alerta}+{x}+{y}"
    )

    # Fundo
    fr_fundo = ctk.CTkFrame(
        master=alerta,
        fg_color="#FFF5F5",
        border_color="#F2B8B8",
        border_width=2,
        corner_radius=8
    )

    fr_fundo.pack(
        fill="both",
        expand=True
    )

    # Título
    lb_titulo = ctk.CTkLabel(
        master=fr_fundo,
        text=titulo,
        font=("Inter", 16, "bold"),
        text_color="#D93036"
    )

    lb_titulo.pack(
        pady=(15, 5)
    )

    # Mensagem
    lb_mensagem = ctk.CTkLabel(
        master=fr_fundo,
        text=mensagem,
        font=("Inter", 13),
        text_color="#18344A"
    )

    lb_mensagem.pack(
        pady=(0, 20)
    )

    # Fechar
    def fechar_alerta():
        alerta.grab_release()
        alerta.destroy()
        parent.focus_force()

    # Botão
    btn_ok = ctk.CTkButton(
        master=fr_fundo,
        text="Tentar Novamente",
        width=130,
        height=32,
        cursor = 'hand2',
        font=("Inter", 12, "bold"),
        fg_color="#D93036",
        hover_color="#B9272D",
        text_color = '#FFFFFF',
        command=fechar_alerta
    )

    btn_ok.pack()

    # Só mostra depois de tudo pronto
    alerta.update_idletasks()
    alerta.deiconify()
    alerta.lift()
    alerta.focus_force()
    alerta.grab_set()