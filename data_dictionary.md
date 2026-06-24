# Data Dictionary

## fund_master

| Column | Type | Description |
|----------|----------|----------|
| amfi_code | INTEGER | AMFI Scheme Code |
| fund_house | TEXT | Mutual Fund Company |
| scheme_name | TEXT | Fund Name |
| category | TEXT | Fund Category |

## nav_history

| Column | Type |
|----------|----------|
| amfi_code | INTEGER |
| date | DATE |
| nav | REAL |

## investor_transactions

| Column | Type |
|----------|----------|
| investor_id | TEXT |
| transaction_date | DATE |
| amfi_code | INTEGER |
| transaction_type | TEXT |
| amount_inr | REAL |

## scheme_performance

| Column | Type |
|----------|----------|
| alpha | REAL |
| beta | REAL |
| sharpe_ratio | REAL |
| expense_ratio_pct | REAL |
| aum_crore | REAL |