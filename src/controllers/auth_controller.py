def validar_login(usuario, senha):
  usuario_correto = "admin"
  senha_correta = "1234"

  if not usuario or not senha:
    return False, "Preencha todos os campos."

  if usuario == usuario_correto and senha == senha_correta:
    return True, "Login realizado com sucesso!"
  else:
    return False, "Usuário ou senha incorretos."