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

    df_limpo["regiao"] = df_limpo["regiao"].str.strip().str.title()

    df_limpo["vendedor"] = df_limpo["vendedor"].str.strip()

    df_limpo.loc[
        df_limpo["categoria"] == "informatica", "categoria"
    ] = "Informática"

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

    df_limpo["faturamento"] = (
        df_limpo["quantidade"] 
        * df_limpo["preco_unitario"] 
        * (1 - df_limpo["desconto"])
    )

    return df_limpo

def calcular_indicadores(df_limpo):
    indicadores = {
        "faturamento_calculavel": df_limpo["faturamento"].sum(),
        "quantidade_total": df_limpo["quantidade"].sum()
    }
    
    return indicadores

def calcular_produto_mais_vendido(df_limpo):
    quantidade_produtos = df_limpo.groupby("produto")["quantidade"].sum()

    produto_mais_vendido_nome = quantidade_produtos.idxmax()
    produto_mais_vendido_valor = quantidade_produtos.max()

    return produto_mais_vendido_nome, produto_mais_vendido_valor


def calcular_produto_menos_vendido(df_limpo):
    quantidade_produtos = df_limpo.groupby("produto")["quantidade"].sum()

    produto_menos_vendido_nome = quantidade_produtos.idxmin()
    produto_menos_vendido_valor = quantidade_produtos.min()

    return produto_menos_vendido_nome, produto_menos_vendido_valor

def calcular_regiao(df_limpo):
    faturamento_regiao = df_limpo.groupby("regiao")["faturamento"].sum()

    regiao_maior_faturamento_nome = faturamento_regiao.idxmax()
    regiao_maior_faturamento_valor = faturamento_regiao.max()

    return regiao_maior_faturamento_nome, regiao_maior_faturamento_valor

def exibir_resultados(
    indicadores,
    regiao,
    faturamento,
    produto,
    quantidade,
    produto_menos,
    quantidade_menos
):
    print("-- Indicadores comerciais --")
    print()
    print(indicadores)
    print()    
    print("Região de maior faturamento:",regiao)
    print("Faturamento da região:",faturamento)
    print()
    print("Produto mais vendido:",produto)
    print("Quantidade vendida:",quantidade)
    print()
    print("Produto menos vendido:",produto_menos)
    print("Quantidade vendida:",quantidade_menos)

def salvar_dados(df, caminho):
    df.to_csv(caminho, index=False)
    

def main():
    df = carregar_dados("dados/vendas_brutas.csv")

    df_limpo = limpar_dados(df)

    #df_limpo.info()

    print(
        df_limpo[
            ["quantidade", "preco_unitario", "desconto", "faturamento"]
        ].head(10)
    )

    indicadores = calcular_indicadores(df_limpo)
    produto, quantidade = calcular_produto_mais_vendido(df_limpo)
    regiao, faturamento = calcular_regiao(df_limpo)
    produto_menos, quantidade_menos = calcular_produto_menos_vendido(df_limpo)

    exibir_resultados(
    indicadores,
    regiao,
    faturamento,
    produto,
    quantidade,
    produto_menos,
    quantidade_menos
    )

    salvar_dados(df_limpo, "dados/vendas_tratadas.csv")

if __name__ == "__main__":
    main()