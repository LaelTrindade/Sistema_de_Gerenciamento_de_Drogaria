from src.database.database_svc import criar_tabelas
from src.views.main_screen_vws import iniciar_app

def main():

    criar_tabelas()
    iniciar_app()
    

if __name__ == "__main__":

    main()