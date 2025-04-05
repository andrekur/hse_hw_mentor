""" Фильтрация хороших валют и подсчет трат по каждой валюте """
result = spark.sql('''
  SELECT 
    currency,
    ROUND(SUM(amount), 2) AS total_amount,
    COUNT(*) AS transaction_count
  FROM temp.transactions
  WHERE currency IN ('USD', 'EUR', 'RUB')
    AND is_fraud = FALSE
    AND amount > 0
  GROUP BY currency
  ORDER BY total_amount DESC
''')
result.show()


""" Расчет нормальных/мошеннических операций по Валютам ('USD', 'EUR', 'RUB') """
result = spark.sql('''
SELECT 
    is_fraud,
    currency,
    COUNT(*) AS transaction_count,
    ROUND(SUM(amount), 2) AS total_amount,
    ROUND(AVG(amount), 2) AS avg_amount,
FROM temp.transactions
WHERE currency IN ('USD', 'EUR', 'RUB') AND amount > 0
GROUP BY currency, is_fraud
ORDER BY currency DESC
''')
result.show(truncate=False)

""" Расчет агрегаций операций по дням и валютам """
result = spark.sql('''
SELECT 
    currency,
    DATE(transaction_date) AS transaction_day,
    COUNT(*) AS transactions_count,
    ROUND(SUM(amount), 2) AS daily_total,
    ROUND(AVG(amount), 2) AS daily_avg,
    ROUND(SUM(CASE WHEN is_fraud = TRUE THEN amount ELSE 0 END), 2) AS fraud_amount,
    SUM(CASE WHEN is_fraud = TRUE THEN 1 ELSE 0 END) AS fraud_count
FROM temp.transactions
WHERE amount > 0
GROUP BY DATE(transaction_date), currency
ORDER BY transaction_day DESC
''')
result.show(truncate=False)


""" Информация по транзакциям с разбивкой по годам/месяцам/неделям/дням/день_недели/части_суток """
result = spark.sql("""
SELECT
  transaction_id,
  amount,
  currency,
  transaction_date,
  DATE(transaction_date) AS transaction_date_only,
  YEAR(transaction_date) AS year,
  MONTH(transaction_date) AS month,
  WEEKOFYEAR(transaction_date) AS week,
  DAYOFMONTH(transaction_date) AS day,
  HOUR(transaction_date) AS hour,
  DAYOFWEEK(transaction_date) AS day_of_week,
  CASE 
    WHEN HOUR(transaction_date) BETWEEN 6 AND 10 THEN 'Утро (6-10)'
    WHEN HOUR(transaction_date) BETWEEN 10 AND 18 THEN 'День (10-18)'
    WHEN HOUR(transaction_date) BETWEEN 18 AND 24 THEN 'Вечер (18-24)'
    ELSE 'Ночь (0-6)'
  END AS day_period
FROM temp.transactions
""")
result.show(truncate=False)


""" Топ категорий по мошенническим операциям """
result = spark.sql("""
SELECT 
    l.category,
    currency,
    COUNT(*) AS count_fraud,
    ROUND(AVG(t.amount), 2) AS avg_fraud_amount
FROM temp.transactions t
JOIN temp.logs l ON t.transaction_id = l.transaction_id
WHERE t.is_fraud = TRUE
  AND l.category IS NOT NULL
  AND t.amount > 0
GROUP BY l.category, currency
ORDER BY count_fraud DESC
LIMIT 10
""")
result.show(truncate=False)