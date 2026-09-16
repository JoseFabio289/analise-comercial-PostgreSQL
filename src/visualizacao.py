import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter


def formatar_reais(valor, posicao):
    return f"R$ {valor:,.0f}".replace(",", ".")


def grafico_faturamento_regiao(df):
    faturamento_regiao = (
        df.groupby("regiao")["faturamento"]
        .sum()
        .sort_values(ascending=False)
    )

    barras = plt.bar(
        faturamento_regiao.index,
        faturamento_regiao.values
    )

    plt.title("Faturamento por Região")
    plt.xlabel("Regiões")
    plt.ylabel("Faturamento (R$)")

    plt.gca().yaxis.set_major_formatter(
        FuncFormatter(formatar_reais)
    )

    plt.bar_label(
        barras,
        fmt=lambda valor: f"R$ {valor:,.0f}".replace(",", ".")
    )

    plt.tight_layout()
    plt.savefig(
        "graficos/faturamento_regiao.png",
        dpi=150,
        bbox_inches="tight"
    )

    plt.show()


def grafico_faturamento_mensal(df):
    df = df.copy()

    df["data"] = pd.to_datetime(df["data"])
    df["mes"] = df["data"].dt.month

    faturamento_mensal = (
        df.groupby("mes")["faturamento"]
        .sum()
    )

    plt.plot(
        faturamento_mensal.index,
        faturamento_mensal.values,
        marker="o"
    )

    plt.title("Faturamento Mensal")
    plt.xlabel("Meses")
    plt.ylabel("Faturamento (R$)")

    plt.xticks(
        [1, 2, 3, 4, 5, 6],
        ["Jan", "Fev", "Mar", "Abr", "Mai", "Jun"]
    )

    plt.gca().yaxis.set_major_formatter(
        FuncFormatter(formatar_reais)
    )

    plt.tight_layout()
    plt.savefig(
        "graficos/faturamento_mensal.png",
        dpi=150,
        bbox_inches="tight"
    )

    plt.show()

def grafico_quantidade_produto(df):
    quantidade_produto = (
        df.groupby("produto")["quantidade"]
        .sum()
        .sort_values(ascending=False)
    )

    barras = plt.bar(
        quantidade_produto.index,
        quantidade_produto.values
    )

    plt.title("Quantidade Vendida por Produto")
    plt.xlabel("Produtos")
    plt.ylabel("Quantidade Vendida")

    plt.bar_label(
        barras,
        fmt="%.0f"
    )

    plt.tight_layout()
    plt.savefig(
        "graficos/quantidade_produto.png",
        dpi=150,
        bbox_inches="tight"
    )

    plt.show()