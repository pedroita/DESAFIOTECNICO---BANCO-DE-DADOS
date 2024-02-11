
-- Operadoras com maiores despesas no ano de 2023 
SELECT operadoras_ativas.REGISTRO_ANS, operadoras_ativas.RAZAO_SOCIAL, SUM(demonstracoes_contabeis2023.VL_SALDO_FINAL) AS 'SOMA'
FROM operadoras_ativas 
INNER JOIN demonstracoes_contabeis2023 ON operadoras_ativas.REGISTRO_ANS = demonstracoes_contabeis2023.REG_ANS
WHERE demonstracoes_contabeis2023.DESCRICAO LIKE '%EVENTOS INDENIZÁVEIS LÍQUIDOS / SINISTROS RETIDOS%'
AND demonstracoes_contabeis2023.DATA BETWEEN '2023-01-01' AND '2023-07-01' -- Filtrando o período de 01/01/2023 a 01/07/2023
GROUP BY operadoras_ativas.REGISTRO_ANS, operadoras_ativas.RAZAO_SOCIAL
ORDER BY SUM(demonstracoes_contabeis2023.VL_SALDO_FINAL) DESC
LIMIT 10;