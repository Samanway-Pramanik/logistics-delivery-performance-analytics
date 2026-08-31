# Total orders

TOTAL_ORDERS = """
SELECT COUNT(*) AS total_orders
FROM orders;
"""


# Total shipments

TOTAL_SHIPMENTS = """
SELECT COUNT(*) AS total_shipments
FROM shipments;
"""


# Shipment status

SHIPMENT_STATUS = """
SELECT
    status,
    COUNT(*) AS shipment_count
FROM shipments
GROUP BY status
ORDER BY shipment_count DESC;
"""


# Orders by warehouse

ORDERS_BY_WAREHOUSE = """
SELECT
    w.warehouse_name,
    COUNT(o.o_id) AS total_orders
FROM warehouses w
JOIN orders o
    ON w.warehouse_id = o.warehouse_id
GROUP BY w.warehouse_name
ORDER BY total_orders DESC;
"""


# Orders by destination city

ORDERS_BY_CITY = """
SELECT
    l.city,
    COUNT(o.o_id) AS total_orders
FROM orders o
JOIN locations l
    ON o.destination_location_id = l.location_id
GROUP BY l.city
ORDER BY total_orders DESC;
"""


# Delivery partner performance

PARTNER_PERFORMANCE = """
SELECT
    dp.partner_name,
    COUNT(s.shipment_id) AS total_shipments
FROM delivery_partners dp
JOIN shipments s
    ON dp.partner_id = s.partner_id
GROUP BY dp.partner_name
ORDER BY total_shipments DESC;
"""