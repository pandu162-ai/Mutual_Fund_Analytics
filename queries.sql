-- Top 5 funds by AUM
SELECT scheme_name,aum_crore
FROM fact_performance
ORDER BY aum_crore DESC
LIMIT 5;

-- Average NAV
SELECT AVG(nav)
FROM fact_nav;

-- SIP transactions
SELECT COUNT(*)
FROM fact_transactions
WHERE transaction_type='SIP';

-- Expense ratio below 1%
SELECT scheme_name
FROM fact_performance
WHERE expense_ratio_pct < 1;

-- Transactions by state
SELECT state,
COUNT(*)
FROM fact_transactions
GROUP BY state;

-- Top alpha
SELECT scheme_name,alpha
FROM fact_performance
ORDER BY alpha DESC
LIMIT 5;

-- Top sharpe ratio
SELECT scheme_name,sharpe_ratio
FROM fact_performance
ORDER BY sharpe_ratio DESC
LIMIT 5;

-- Risk grade count
SELECT risk_grade,
COUNT(*)
FROM fact_performance
GROUP BY risk_grade;

-- Average expense ratio
SELECT AVG(expense_ratio_pct)
FROM fact_performance;

-- Highest AUM
SELECT scheme_name,aum_crore
FROM fact_performance
ORDER BY aum_crore DESC
LIMIT 10;