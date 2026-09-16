-- Faturamento total calculável --

SELECT 
    SUM(quantidade * preco_unitario * (1 - desconto)) AS faturamento_total_calculavel
FROM vendas;

-- Faturamento por região --

SELECT 
    regiao, SUM(quantidade * preco_unitario * (1 - desconto)) AS faturamento_total
	FROM vendas
WHERE regiao IS NOT NULL
GROUP BY regiao
ORDER BY faturamento_total DESC;

-- Região com maior faturamento --

SELECT 
    regiao, SUM(quantidade * preco_unitario * (1 - desconto)) AS faturamento_
	FROM vendas
WHERE regiao IS NOT NULL
GROUP BY regiao
ORDER BY faturamento_total DESC
LIMIT 1;

-- Região com menor faturamento --

SELECT 
    regiao, SUM(quantidade * preco_unitario * (1 - desconto)) AS faturamento_regiao
	FROM vendas
WHERE regiao IS NOT NULL
GROUP BY regiao
ORDER BY faturamento_total ASC
LIMIT 1;

-- Produto mais vendido --

SELECT 
    Produto, SUM(quantidade) AS vendas_totais
    FROM vendas
WHERE produto IS NOT NULL
GROUP BY Produto
ORDER BY vendas_totais DESC
LIMIT 1;

-- Produto menos vendido --

SELECT 
    Produto, SUM(quantidade) AS vendas_totais
    FROM vendas
WHERE produto IS NOT NULL
GROUP BY Produto
ORDER BY vendas_totais ASC
LIMIT 1;

-- Vendedor com maior faturamento --

SELECT 
    Vendedor, SUM(Quantidade * preco_unitario * (1 - desconto)) AS faturamento_vendedor
    FROM vendas
WHERE Vendedor IS NOT NULL
GROUP BY Vendedor
ORDER BY faturamento_vendedor
LIMIT 1;


-- Faturamento mensal --

SELECT
    DATE_TRUNC('month', data) AS mes, SUM(Quantidade * preco_unitario * (1 - desconto)) AS faturamento_mes
    FROM vendas
GROUP BY mes
ORDER BY faturamento_mes DESC;

-- Quantidade de produtos vendidos por mês --

SELECT
    DATE_TRUNC('month', data) AS mes, SUM(Quantidade) AS quantidade_mes
    FROM vendas
GROUP BY mes
ORDER BY mes;

-- Média de preço unitário mensal --

SELECT
    DATE_TRUNC('month', data) AS mes, AVG(preco_unitario) AS media_preco_unitario_mes
    FROM vendas
GROUP BY mes
ORDER BY mes;

-- Média de desconto mensal --

SELECT
    DATE_TRUNC('month', data) AS mes, AVG(desconto) AS media_desconto_mes
    FROM vendas
GROUP BY mes
ORDER BY mes;