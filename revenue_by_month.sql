-- 3. Query Writing Challenge: Consider a table orders with columns order_id, customer_id, order_date, and total_amount. Write a SQL query to calculate the total revenue generated in the last quarter, grouped by month.

SELECT 
    DATE_TRUNC('month', order_date) AS month,
    SUM(total_amount) AS total_revenue
FROM 
    orders
WHERE 
    order_date >= DATE_TRUNC('quarter', CURRENT_DATE) - INTERVAL '3 months'
GROUP BY 
    month
ORDER BY 
    month;
