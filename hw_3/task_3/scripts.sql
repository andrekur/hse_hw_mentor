
-- График продаж за неделю
-- Параметры (date_start, date_end) интервал фильтрации
-- По дефолту 7 дней назад от текущей даты
SELECT 
    DATE(order_date) AS day,
    CAST(ROUND(SUM(total_amount), 2) AS Int32) daily_revenue
FROM default.Orders
WHERE DATE(order_date) >= {{date_start}} AND DATE(order_date) <= {{date_end}}
GROUP BY DATE(order_date)
ORDER BY day DESC;


-- Топ-5 товаров по обороту
-- Параметры (date_order_start, date_order_end) интервал фильтрации
-- По дефолту период 30 дней назад от текущей даты
SELECT 
    oi.product_name,
    CAST(ROUND(SUM(oi.product_price * oi.quantity), 2) AS Int32) daily_revenue
FROM default.OrderItems oi
JOIN default.Orders o ON oi.order_id = o.order_id
WHERE o.payment_status = 'paid'
AND o.order_date >= {{date_order_start}}
AND o.order_date <= {{date_order_end}}
GROUP BY oi.product_name
ORDER BY daily_revenue DESC
LIMIT 5;


-- Статистика по статусам заказов
-- Параметр date_status дата для фильтрации
-- По дефолту текущая дата
SELECT 
    o.payment_status,
    CAST(SUM(oi.product_price * oi.quantity) AS Int32) as gross
FROM default.Orders o
JOIN default.OrderItems oi ON o.order_id = oi.order_id
WHERE DATE(order_date) = {{date_status}}
GROUP BY o.payment_status
ORDER BY gross DESC;