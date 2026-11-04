import bcrypt
from src.database.database_svc import conectar


def carregar_usuarios():
  """Lê a lista de usuários do banco."""
  with conectar() as conexao:
    linhas = conexao.execute("SELECT * FROM usuarios").fetchall()

  usuarios = []

  for linha in linhas:
    usuario = dict(linha)
    usuario["ativo"] = bool(usuario["ativo"])
    usuarios.append(usuario)

  return usuarios


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