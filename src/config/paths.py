from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# Caminho das Imagens
ASSETS_IMAGES = BASE_DIR/'assets'/'images'/'icons'
IMAGES_LOGIN_SCREEN = ASSETS_IMAGES/'login_screen'
IMAGES_MAIN_SCREEN = ASSETS_IMAGES/'main_screen'
IMAGES_DASHBOARD = ASSETS_IMAGES/'dashboard'

# Caminho dos JSONs
CAMINHO_USERS_JSON = BASE_DIR/'database'/'users_database.json'
CAMINHO_DASHBOARD_JSON = BASE_DIR/"database"/"dashboard_database.json"