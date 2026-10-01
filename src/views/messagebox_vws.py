import customtkinter as ctk

def exibir_messagebox(parent, titulo, mensagem):
    alerta = ctk.CTkToplevel(parent)
    

    alerta.overrideredirect(True)
    alerta.geometry("350x160")

    
    alerta.transient(parent)
    alerta.grab_set()
    
#essa linha aqui pessoal faz com o que o usuario so preencha os campos novamente apos clicar em tente novamente no alerta 
    parent.update_idletasks()
    
    largura_alerta = 350
    altura_alerta = 160
    
    x = parent.winfo_x() + (parent.winfo_width() // 2) - (largura_alerta // 2)
    y = parent.winfo_y() + (parent.winfo_height() // 2) - (altura_alerta // 2)
    
    alerta.geometry(f"{largura_alerta}x{altura_alerta}+{x}+{y}")

   
    fr_fundo = ctk.CTkFrame(
        master=alerta, 
        fg_color="#FFF1F1", 
        border_color="#F3B8BA", 
        border_width=2, 
        corner_radius=8
    )
    fr_fundo.pack(fill="both", expand=True)

   
    lb_titulo = ctk.CTkLabel(
        master=fr_fundo, 
        text=titulo, 
        font=('Inter', 16, 'bold'), 
        text_color="#E02A2A" 
    )
    lb_titulo.pack(pady=(15, 5))

   
    lb_mensagem = ctk.CTkLabel(
        master=fr_fundo, 
        text=mensagem, 
        font=('Inter', 13), 
        text_color="#18344A"
    )
    lb_mensagem.pack(pady=(0, 20))


    def fechar_alerta():
        alerta.grab_release() 
        alerta.destroy()      
        parent.focus_force()  

    
    btn_ok = ctk.CTkButton(
        master=fr_fundo, 
        text="Tentar Novamente", 
        width=130,
        height=32,
        font=('Inter', 12, 'bold'),
        fg_color="#E02A2A", 
        hover_color="#B32020",
        command=fechar_alerta 
    )
    btn_ok.pack()