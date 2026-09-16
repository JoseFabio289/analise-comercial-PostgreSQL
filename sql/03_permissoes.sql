-- Permissões minimas necessárias para o usuário da aplicação.
-- O usuário app_vendas deve ser criado previamente pelo administrador.

GRANT SELECT, INSERT
ON TABLE public.vendas
TO app_vendas;