from src.tratamento import (
    carregar_dados,
    diagnosticar_dados,
    limpar_dados,
    salvar_dados
)

from src.analise import (
    calcular_indicadores,
    calcular_produto_mais_vendido,
    calcular_produto_menos_vendido,
    calcular_regiao,
    exibir_resultados
)

from src.banco import (
    inserir_dados,
    conectar_banco,
    preparar_dados_banco
)

def main():
    df = carregar_dados("dados/vendas_brutas.csv")

    diagnosticar_dados(df)

    df_limpo = limpar_dados(df)

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

    registros = preparar_dados_banco(df_limpo)

    conexao = conectar_banco()

    try:
        inserir_dados(conexao, registros)
    finally:
        conexao.close()

if __name__ == "__main__":
    main()