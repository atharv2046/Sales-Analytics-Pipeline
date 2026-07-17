-- Business Question:
-- Which customers placed which orders?

SELECT
    c.customer_id,
    c.customer_city,
    c.customer_state,
    o.order_id,
    o.order_status
FROM customers c
JOIN orders o
ON c.customer_id = o.customer_id;


-- Business Question:
-- Which customers spent the most?

SELECT
    c.customer_id,
    ROUND(SUM(p.payment_value),2) AS total_spent
FROM customers c
JOIN orders o
ON c.customer_id = o.customer_id
JOIN payments p
ON o.order_id = p.order_id
GROUP BY c.customer_id
ORDER BY total_spent DESC
LIMIT 10;

-- Business Question:
-- Which product categories generate the highest revenue?

SELECT
    pr.product_category_name_english,
    ROUND(SUM(oi.price),2) AS revenue
FROM order_items oi
JOIN products pr
ON oi.product_id = pr.product_id
GROUP BY pr.product_category_name_english
ORDER BY revenue DESC;


-- Business Question:
-- Which products are sold the most?

SELECT
    product_id,
    COUNT(*) AS total_sales
FROM order_items
GROUP BY product_id
ORDER BY total_sales DESC
LIMIT 10;

-- Business Question:
-- Which sellers generated the highest revenue?

SELECT
    s.seller_id,
    ROUND(SUM(oi.price),2) AS revenue
FROM sellers s
JOIN order_items oi
ON s.seller_id = oi.seller_id
GROUP BY s.seller_id
ORDER BY revenue DESC
LIMIT 10;

-- Business Question:
-- Which seller states generate the highest revenue?

SELECT
    s.seller_state,
    ROUND(SUM(oi.price),2) AS revenue
FROM sellers s
JOIN order_items oi
ON s.seller_id = oi.seller_id
GROUP BY s.seller_state
ORDER BY revenue DESC;

-- Business Question:
-- Which product categories receive the highest ratings?

SELECT
    pr.product_category_name_english,
    ROUND(AVG(r.review_score),2) AS avg_rating
FROM reviews r
JOIN orders o
ON r.order_id = o.order_id
JOIN order_items oi
ON o.order_id = oi.order_id
JOIN products pr
ON oi.product_id = pr.product_id
GROUP BY pr.product_category_name_english
ORDER BY avg_rating DESC;


-- Business Question:
-- Which cities place the most orders?

SELECT
    c.customer_city,
    COUNT(o.order_id) AS total_orders
FROM customers c
JOIN orders o
ON c.customer_id = o.customer_id
GROUP BY c.customer_city
ORDER BY total_orders DESC
LIMIT 20;

-- Business Question:
-- Which states have the fastest deliveries?

SELECT
    c.customer_state,
    ROUND(AVG(o.delivery_days),2) AS avg_delivery_days
FROM customers c
JOIN orders o
ON c.customer_id = o.customer_id
GROUP BY c.customer_state
ORDER BY avg_delivery_days;

-- Business Question:
-- How much revenue comes from each payment method?

SELECT
    payment_type,
    ROUND(SUM(payment_value),2) AS revenue
FROM payments
GROUP BY payment_type
ORDER BY revenue DESC;

-- Business Question:
-- How does revenue change over time?

SELECT
    o.purchase_year,
    o.purchase_month,
    ROUND(SUM(p.payment_value),2) AS revenue
FROM orders o
JOIN payments p
ON o.order_id = p.order_id
GROUP BY o.purchase_year, o.purchase_month
ORDER BY o.purchase_year, o.purchase_month;

-- Business Question:
-- Which customers placed the most orders?

SELECT
    c.customer_id,
    COUNT(o.order_id) AS total_orders
FROM customers c
JOIN orders o
ON c.customer_id = o.customer_id
GROUP BY c.customer_id
ORDER BY total_orders DESC
LIMIT 10;

-- Business Question:
-- Which sellers incur the highest freight costs?

SELECT
    s.seller_id,
    ROUND(SUM(oi.freight_value),2) AS freight_cost
FROM sellers s
JOIN order_items oi
ON s.seller_id = oi.seller_id
GROUP BY s.seller_id
ORDER BY freight_cost DESC
LIMIT 10;


-- Business Question:
-- Which product categories generate the most revenue in each state?

SELECT
    c.customer_state,
    pr.product_category_name_english,
    ROUND(SUM(oi.price),2) AS revenue
FROM customers c
JOIN orders o
ON c.customer_id = o.customer_id
JOIN order_items oi
ON o.order_id = oi.order_id
JOIN products pr
ON oi.product_id = pr.product_id
GROUP BY c.customer_state, pr.product_category_name_english
ORDER BY revenue DESC;

-- Business Question:
-- What are the overall business KPIs?

SELECT
    COUNT(DISTINCT o.order_id) AS total_orders,
    COUNT(DISTINCT c.customer_id) AS total_customers,
    ROUND(SUM(p.payment_value),2) AS total_revenue,
    ROUND(AVG(r.review_score),2) AS average_rating
FROM customers c
JOIN orders o
ON c.customer_id = o.customer_id
JOIN payments p
ON o.order_id = p.order_id
JOIN reviews r
ON o.order_id = r.order_id;

