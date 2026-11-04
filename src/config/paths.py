from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# Caminho das Imagens
ASSETS_IMAGES = BASE_DIR/'assets'/'images'/'icons'
IMAGES_MESSAGEBOX = ASSETS_IMAGES/'messagebox'
IMAGES_LOGIN_SCREEN = ASSETS_IMAGES/'login_screen'
IMAGES_MAIN_SCREEN = ASSETS_IMAGES/'main_screen'
IMAGES_DASHBOARD = ASSETS_IMAGES/'dashboard'
IMAGES_MEDICAMENTOS = ASSETS_IMAGES/'medicamentos'


# Caminho do Banco de Dados (SQLite)
CAMINHO_DATABASE = BASE_DIR / 'database' / 'trustmed.db'
CAMINHO_DASHBOARD_JSON = BASE_DIR/'database'/'dashboard_database.json'