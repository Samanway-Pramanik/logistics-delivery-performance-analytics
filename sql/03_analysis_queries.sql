-- 1. Total number of orders

SELECT
    COUNT(*) AS total_orders
FROM orders;


-- 2. Orders handled by each warehouse

SELECT
    w.warehouse_name,
    COUNT(o.o_id) AS total_orders
FROM warehouses w
JOIN orders o
    ON w.warehouse_id = o.warehouse_id
GROUP BY w.warehouse_name
ORDER BY total_orders DESC;


-- 3. Orders by destination city

SELECT
    l.city,
    COUNT(o.o_id) AS total_orders
FROM orders o
JOIN locations l
    ON o.destination_location_id = l.location_id
GROUP BY l.city
ORDER BY total_orders DESC;


-- 4. Average order value by priority

SELECT
    priority,
    ROUND(AVG(o_value), 2) AS average_order_value
FROM orders
GROUP BY priority
ORDER BY average_order_value DESC;


-- 5. Delivery partner performance

SELECT
    dp.partner_name,
    COUNT(s.shipment_id) AS total_shipments
FROM delivery_partners dp
JOIN shipments s
    ON dp.partner_id = s.partner_id
GROUP BY dp.partner_name
ORDER BY total_shipments DESC;


-- 6. Delayed shipments

SELECT
    shipment_id,
    o_id,
    partner_id,
    dispatch_date,
    expected_delivery_date,
    actual_delivery_date,
    delivery_attempts
FROM shipments
WHERE status = 'Delayed'
ORDER BY actual_delivery_date;


-- 7. Average delivery time by delivery partner

SELECT
    dp.partner_name,
    ROUND(
        AVG(s.actual_delivery_date - s.dispatch_date),
        2
    ) AS average_delivery_days
FROM delivery_partners dp
JOIN shipments s
    ON dp.partner_id = s.partner_id
GROUP BY dp.partner_name
ORDER BY average_delivery_days;


-- 8. Delivery performance by status

SELECT
    status,
    COUNT(*) AS shipment_count
FROM shipments
GROUP BY status
ORDER BY shipment_count DESC;


-- 9. Warehouse ranking by number of orders
-- Using RANK() window function

WITH warehouse_orders AS (

    SELECT
        w.warehouse_name,
        COUNT(o.o_id) AS total_orders
    FROM warehouses w
    JOIN orders o
        ON w.warehouse_id = o.warehouse_id
    GROUP BY w.warehouse_name
)

SELECT
    warehouse_name,
    total_orders,
    RANK() OVER (
        ORDER BY total_orders DESC
    ) AS warehouse_rank
FROM warehouse_orders
ORDER BY warehouse_rank;


-- 10. Monthly shipment volume
-- Using a simple date function

SELECT
    DATE_TRUNC('month', dispatch_date) AS month,
    COUNT(*) AS total_shipments
FROM shipments
GROUP BY month
ORDER BY month;


-- 11. Month-to-month shipment comparison
-- Using LAG() window function

WITH monthly_shipments AS (

    SELECT
        DATE_TRUNC('month', dispatch_date) AS month,
        COUNT(*) AS total_shipments
    FROM shipments
    GROUP BY month
)

SELECT
    month,
    total_shipments,
    LAG(total_shipments) OVER (
        ORDER BY month
    ) AS previous_month_shipments
FROM monthly_shipments
ORDER BY month;


-- 12. Orders with multiple delivery attempts

SELECT
    shipment_id,
    o_id,
    delivery_attempts,
    status
FROM shipments
WHERE delivery_attempts > 1
ORDER BY delivery_attempts DESC;