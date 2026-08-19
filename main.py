import pandas as pd

pd.set_option('display.max_columns', None)

def carregar_dados(caminho):
    return pd.read_csv(caminho)


def diagnosticar_dados(df):
    print("--- Diagnóstico dos dados ---")
    print()

    print("Valores ausentes por coluna:")
    print(df.isna().sum())
    print()

    print("Duplicatas completas:")
    print(df.duplicated().sum())
    print()

    print("Quantidade negativa:")
    print((df["quantidade"] < 0).sum())
    print()

    print("Preço unitário negativo:")
    print((df["preco_unitario"] < 0).sum())
    print()

    filtro_desconto_invalido = (
        (df["desconto"] < 0) |
        (df["desconto"] > 1)
    )

    print("Descontos inválidos:")
    print(filtro_desconto_invalido.sum())
    

def limpar_dados(df):
    df_limpo = df.drop_duplicates()

    df_limpo.loc[
        df_limpo["quantidade"] < 0,
        "quantidade"
    ] = pd.NA

    df_limpo.loc[
        df_limpo["preco_unitario"] < 0,
        "preco_unitario"
    ] = pd.NA

    df_limpo.loc[
        (df_limpo["desconto"] < 0) |
        (df_limpo["desconto"] > 1),
        "desconto"
    ] = pd.NA

    df_limpo["data"] = pd.to_datetime(df_limpo["data"])

    df_limpo["quantidade"] = df_limpo["quantidade"].astype("Int64")

    return df_limpo

def main():
    df = carregar_dados("dados/vendas_brutas.csv")

    df_limpo = limpar_dados(df)

    df_limpo.info()

if __name__ == "__main__":
    main()