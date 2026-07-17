SELECT
    YEAR(order_purchase_timestamp) AS year,
    MONTH(order_purchase_timestamp) AS month,
    ROUND(SUM(payment_value),2) AS revenue
FROM orders
JOIN payments
ON orders.order_id = payments.order_id
GROUP BY year, month
ORDER BY year, month;



SELECT
    payment_type,
    ROUND(SUM(payment_value),2) AS revenue
FROM payments
GROUP BY payment_type
ORDER BY revenue DESC;

\SELECT
    MONTH(order_purchase_timestamp) AS month,
    COUNT(*) AS total_orders
FROM orders
GROUP BY month
ORDER BY month;


SELECT
    ROUND(AVG(delivery_days),2) AS avg_delivery_days
FROM orders;

SELECT
    customer_state,
    ROUND(SUM(payment_value),2) AS revenue
FROM customers
JOIN orders
ON customers.customer_id = orders.customer_id
JOIN payments
ON orders.order_id = payments.order_id
GROUP BY customer_state
ORDER BY revenue DESC;

