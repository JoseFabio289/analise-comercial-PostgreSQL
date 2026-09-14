create table vendas(
	id_venda integer primary key,
	data date,
	produto text,
	categoria text,
	vendedor text,
	regiao text,
	quantidade integer,
	preco_unitario numeric(10,2),
	desconto numeric(4,3)
		check(desconto >= 0 and desconto <= 1)
);