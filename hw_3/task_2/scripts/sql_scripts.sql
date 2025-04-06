-- Расчет Кол. заказов в каждом статусе/общая сумма/средний чек
SELECT 
    payment_status,
    COUNT(DISTINCT o.order_id) AS orders_count,
    SUM(o.total_amount) AS total_amount_in_status, -- денег в статусе
    ROUND(AVG(o.total_amount), 2) AS avg_order_amount
FROM Orders o
GROUP BY payment_status
ORDER BY total DESC;

-- Расчет статистики по товарам в каждом статусе: количество товаров, средняя цена за продукт, общая сумма.
SELECT 
    o.payment_status,
    COUNT(DISTINCT oi.item_id) AS total_items_sold, -- сумма уникальных товаров в статусе
    SUM(oi.quantity) AS total_quantity, -- кол. товара в статусе
    ROUND(AVG(oi.product_price), 2) AS avg_product_price_in_status,
    SUM(oi.product_price * oi.quantity) AS gross -- стоимость товара
FROM Orders o
JOIN OrderItems oi ON o.order_id = oi.order_id
GROUP BY o.payment_status
ORDER BY total_items_sold DESC;

-- Расчет по обороту по дням, без учета статуса
SELECT 
    DATE(order_date) AS day,
    COUNT(order_id) AS orders_count,
    ROUND(SUM(total_amount), 2) AS daily_revenue,
    ROUND(AVG(total_amount), 2) AS avg_order_value,
    COUNT(DISTINCT user_id) AS unique_customers
FROM Orders
GROUP BY DATE(order_date)
ORDER BY day DESC;

-- Расчет по обороту по дням и статусам заказов
SELECT 
    DATE(order_date) AS day,
    payment_status,
    COUNT(DISTINCT order_id) AS orders_count,
    ROUND(SUM(total_amount), 2) AS daily_revenue,
    COUNT(DISTINCT user_id) AS unique_customers
FROM Orders
GROUP BY DATE(order_date), payment_status
ORDER BY day DESC, daily_revenue DESC;

-- Расчет Топ-5 пользователей по тратам
SELECT 
    user_id,
    ROUND(SUM(total_amount), 2) AS total_spent,
    COUNT(DISTINCT order_id) AS orders_count,
    ROUND(SUM(total_amount) / COUNT(DISTINCT order_id), 2) AS avg_order_value
FROM Orders
WHERE payment_status = 'paid'
GROUP BY user_id
ORDER BY total_spent DESC
LIMIT 5;

-- Расчет Топ-5 товаров по количеству продаж
SELECT 
    oi.product_name,
    COUNT(DISTINCT o.order_id) AS orders_count,
    SUM(oi.quantity) AS total_quantity_sold,
    ROUND(SUM(oi.product_price * oi.quantity), 2) AS total_revenue,
    ROUND(AVG(oi.product_price), 2) AS avg_product_price,
    COUNT(DISTINCT o.user_id) AS unique_customers
FROM OrderItems oi
JOIN Orders o ON oi.order_id = o.order_id
WHERE o.payment_status = 'paid'
GROUP BY oi.product_name
ORDER BY total_quantity_sold DESC
LIMIT 5;