CREATE TABLE gold.customer_summary AS
SELECT
    customer_id,
    COUNT(*) AS total_orders,
    SUM(order_amount) AS total_spent
FROM silver.orders
GROUP BY customer_id;