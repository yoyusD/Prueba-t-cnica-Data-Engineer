CREATE OR REPLACE VIEW monto_total_por_dia AS SELECT
c.company_name, to_char(ch.created_at, 'DD/MM/YYYY') AS transaction_date, SUM(ch.amount) AS total_amount
FROM charges ch JOIN companies c ON ch.company_id = c.company_id
GROUP BY c.company_name, to_char(ch.created_at, 'DD/MM/YYYY')
ORDER BY transaction_date, c.company_name;
