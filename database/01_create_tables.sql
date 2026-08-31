-- Here we will make tables according to the columns in the created .csv files , like -
-- customers.csv


-- locations.csv (location_id,city,region)
CREATE TABLE IF NOT EXISTS locations (
    location_id INTEGER,
    city VARCHAR(20) ,
    region VARCHAR(20) 
);

--warhouses.csv (warhouse_id,warehouse_name,location_id,capacity)
CREATE TABLE IF NOT EXISTS warehouses (
    warehouse_id INTEGER ,
    warehouse_name VARCHAR(30),
    location_id INTEGER ,
    capacity INTEGER 
); 

-- delivery_partners.csv (partner_id,partner_name)
CREATE TABLE IF NOT EXISTS delivery_partners (
    partner_id INTEGER ,
    partner_name VARCHAR(50) 
); 

--customers.csv (c_id,c_name,city,region,c_type)
CREATE TABLE IF NOT EXISTS customers (
    c_id INTEGER,
    c_name VARCHAR(30) ,
    city VARCHAR(30),
    region VARCHAR(30),
    c_type VARCHAR(20) 
);

-- orders.csv (o_id,c_id,warhouse_id,destination_location_id,o_date,o_value,priority) 
CREATE TABLE IF NOT EXISTS orders (
    o_id INTEGER ,
    c_id INTEGER ,
    warehouse_id INTEGER,
    destination_location_id INTEGER ,
    o_date DATE ,
    o_value NUMERIC(10,2) ,
    priority VARCHAR(20) 
);


-- --shipments.csv (shipment_id,o_id,partner_id,dispatch_date,expected_delivery_date,actual_delivery_date,status,delivery_attempts
-- )
CREATE TABLE IF NOT EXISTS shipments (
    shipment_id INTEGER , 
    o_id INTEGER ,
    partner_id INTEGER , 
    dispatch_date DATE , 
    expected_delivery_date DATE , 
    actual_delivery_date DATE ,
    status VARCHAR(30) ,
    delivery_attempts INTEGER 
);

