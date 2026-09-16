import pandas as pd
from src.tratamento import limpar_dados

def test_quantidade_negativa_vira_na():
    df = pd.DataFrame({
    "id_venda": [1],
    "data": ["2026-01-01"],
    "produto": ["Mouse"],
    "categoria": ["Informática"],
    "vendedor": ["Ana"],
    "regiao": ["Sul"],
    "quantidade": [-2],
    "preco_unitario": [100.0],
    "desconto": [0.10]
})

    df_limpo = limpar_dados(df)

    assert pd.isna(df_limpo.loc[0, "quantidade"])

def test_calculo_faturamento():
    df = pd.DataFrame({
        "id_venda": [1],
        "data": ["2026-01-01"],
        "produto": ["Mouse"],
        "categoria": ["Informática"],
        "vendedor": ["Ana"],
        "regiao": ["Sul"],
        "quantidade": [2],
        "preco_unitario": [100.0],
        "desconto": [0.10]
    })

    df_limpo = limpar_dados(df)

    assert df_limpo.loc[0, "faturamento"] == 180

def test_remove_duplicatas():
    df = pd.DataFrame({
        "id_venda": [1, 1],
        "data": ["2026-01-01", "2026-01-01"],
        "produto": ["Mouse", "Mouse"],
        "categoria": ["Informática", "Informática"],
        "vendedor": ["Ana", "Ana"],
        "regiao": ["Sul", "Sul"],
        "quantidade": [2, 2],
        "preco_unitario": [100.0, 100.0],
        "desconto": [0.10, 0.10]
    })

    df_limpo = limpar_dados(df)

    assert len(df_limpo) == 1