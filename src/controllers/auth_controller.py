import json
import bcrypt
from src.config.paths import CAMINHO_USERS_JSON


def carregar_usuarios():
  """Lê a lista de usuários do JSON."""
  if not CAMINHO_USERS_JSON.exists():
    return []

  with open(CAMINHO_USERS_JSON, "r", encoding="utf-8") as arquivo:
    return json.load(arquivo).get("usuarios", [])


def validar_login(usuario, senha):

  if not usuario or not senha:
    return False, "Preencha todos os campos."

  for u in carregar_usuarios():

    if u["login"].lower() == usuario.strip().lower():

      senha_ok = bcrypt.checkpw(
          senha.encode("utf-8"), u["senha_hash"].encode("utf-8")
      )

      if senha_ok and u.get("ativo", True):
        return True, "Login realizado com sucesso!"

      break

  return False, "Usuário ou senha incorretos."