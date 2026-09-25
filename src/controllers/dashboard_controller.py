import json
from pathlib import Path

CAMINHO_JSON = Path(__file__).parent.parent.parent / "database" / "database.json"


def carregar_dados():
  """Lê os dados do arquivo JSON de forma segura."""
  if not CAMINHO_JSON.exists():
    return {
        "faturamento": "R$ 0,00",
        "medicamentos": "0 und",
        "estoque": "0 und",
        "alertas": [],
        "vendas_semana": {
            "dias": ["Seg", "Ter", "Qua", "Qui", "Sex", "Sáb", "Dom"],
            "valores": [0, 0, 0, 0, 0, 0, 0],
        },
        "relatorios": [],
    }

  with open(CAMINHO_JSON, "r", encoding="utf-8") as arquivo:
    return json.load(arquivo)


def salvar_dados(dados):
  """Salva as alterações atualizadas no arquivo JSON."""
  with open(CAMINHO_JSON, "w", encoding="utf-8") as arquivo:
    json.dump(dados, arquivo, ensure_ascii=False, indent=4)


def obter_dados_dashboard():
  """Retorna os dados formatados para preencher a view do dashboard."""
  dados = carregar_dados()

  faturamento = dados.get("faturamento", "R$ 0,00")
  medicamentos = dados.get("medicamentos", "0 und")
  estoque = dados.get("estoque", "0 und")
  alertas = dados.get("alertas", [])

  dias_semana = dados.get("vendas_semana", {}).get(
      "dias", ["Seg", "Ter", "Qua", "Qui", "Sex", "Sáb", "Dom"]
  )
  valores_vendas = dados.get("vendas_semana", {}).get(
      "valores", [0, 0, 0, 0, 0, 0, 0]
  )

  relatorios = [
      (
          item.get("produto"),
          item.get("quantidade"),
          item.get("valor"),
          item.get("horario"),
      )
      for item in dados.get("relatorios", [])
  ]

  return (
      faturamento,
      medicamentos,
      estoque,
      alertas,
      dias_semana,
      valores_vendas,
      relatorios,
  )