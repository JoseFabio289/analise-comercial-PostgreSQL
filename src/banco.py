import pandas as pd
import os
import psycopg
from dotenv import load_dotenv

load_dotenv()

def inserir_dados(conexao, registros):
    sql = """
        INSERT INTO vendas(
            id_venda,
            data,
            produto,
            categoria,
            vendedor,
            regiao,
            quantidade,
            preco_unitario,
            desconto
        )
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        ON CONFLICT (id_venda) DO NOTHING;
    """

    with conexao.cursor() as cursor:
        cursor.executemany(sql, registros)

    conexao.commit()

def conectar_banco():
    return psycopg.connect(
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT"),
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
    )

def preparar_dados_banco(df_limpo):
    colunas_banco = [
        "id_venda",
        "data",
        "produto",
        "categoria",
        "vendedor",
        "regiao",
        "quantidade",
        "preco_unitario",
        "desconto"
    ]

    df_banco = df_limpo[colunas_banco].copy()

    df_banco["data"] = df_banco["data"].dt.date

    registros = []

    for linha in df_banco.itertuples(index=False, name=None):
        registro = tuple(
        None if pd.isna(valor)
        else valor.item() if hasattr(valor, "item")
        else valor.to_pydatetime() if hasattr(valor, "to_pydatetime")
        else valor
        for valor in linha
    )

        registros.append(registro)
    return registros