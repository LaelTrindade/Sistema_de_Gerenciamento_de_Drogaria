from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

ASSETS_IMAGES = BASE_DIR/'assets'/'images'/'icons'
IMAGES_LOGIN_SCREEN = ASSETS_IMAGES/'login_screen'
IMAGES_MAIN_SCREEN = ASSETS_IMAGES/'main_screen'
IMAGES_DASHBOARD = ASSETS_IMAGES/'dashboard'