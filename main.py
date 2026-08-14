import pandas as pd


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


def main():
    df = carregar_dados("dados/vendas_brutas.csv")

    diagnosticar_dados(df)


if __name__ == "__main__":
    main()