-- Faturamento total calculável --

SELECT 
    SUM(quantidade * preco_unitario * (1 - desconto)) 
    AS faturamento_total_calculavel
FROM vendas;

-- Faturamento por região --

SELECT 
    regiao, SUM(quantidade * preco_unitario 
	* (1 - desconto)) AS faturamento_total
	FROM vendas
WHERE regiao IS NOT NULL
GROUP BY regiao
ORDER BY faturamento_total DESC;

-- Região com maior faturamento --

SELECT 
    regiao, SUM(quantidade * preco_unitario 
	* (1 - desconto)) AS faturamento_
	FROM vendas
WHERE regiao IS NOT NULL
GROUP BY regiao
ORDER BY faturamento_total DESC
LIMIT 1;

-- Região com menor faturamento --

SELECT 
    regiao, SUM(quantidade * preco_unitario 
	* (1 - desconto)) AS faturamento_regiao
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