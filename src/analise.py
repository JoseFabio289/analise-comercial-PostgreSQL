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