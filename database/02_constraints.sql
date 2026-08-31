-- primary keys 

ALTER TABLE locations 
ADD CONSTRAINT pk_locations 
PRIMARY KEY (location_id) ; 

ALTER TABLE warehouses 
ADD CONSTRAINT pk_warehouses 
PRIMARY KEY (warehouse_id) ;

ALTER TABLE delivery_partners 
ADD CONSTRAINT pk_delivery_partners 
PRIMARY KEY (partner_id) ;

ALTER TABLE customers 
ADD CONSTRAINT pk_customers 
PRIMARY KEY (c_id);

ALTER TABLE orders 
ADD CONSTRAINT pk_orders 
PRIMARY KEY (o_id) ;

ALTER TABLE shipments 
ADD CONSTRAINT pk_shipments 
PRIMARY KEY (shipment_id) ;


-- Foreign Keys 

ALTER TABLE warehouses 
ADD CONSTRAINT fk_warehouse_location 
FOREIGN KEY (location_id) 
REFERENCES locations(location_id) ;

ALTER TABLE orders 
ADD CONSTRAINT fk_order_warehouse 
FOREIGN KEY (warehouse_id) 
REFERENCES warehouses(warehouse_id) ;

ALTER TABLE orders 
ADD CONSTRAINT fk_order_customer 
FOREIGN KEY (c_id) 
REFERENCES customers(c_id) ;

ALTER TABLE orders 
ADD CONSTRAINT fk_order_location  --fk_order_destination 
FOREIGN KEY (destination_location_id) 
REFERENCES locations(location_id) ;

ALTER TABLE shipments 
ADD CONSTRAINT fk_shipment_order 
FOREIGN KEY (o_id) 
REFERENCES orders(o_id) ;

ALTER TABLE shipments 
ADD CONSTRAINT fk_shipment_delivery_partner 
FOREIGN KEY (partner_id) 
REFERENCES delivery_partners(partner_id) ;



-- NOT NULL CONSTRAINTS 

-- locations.csv (location_id,city,region)
--warehouses.csv (warehouse_id,warehouse_name,location_id,capacity)
-- delivery_partners.csv (partner_id,partner_name)
--customers.csv (c_id,c_name,city,region,c_type)
-- orders.csv (o_id,c_id,warhouse_id,destination_location_id,o_date,o_value,priority) 
-- --shipments.csv (shipment_id,o_id,partner_id,dispatch_date,expected_delivery_date,actual_delivery_date,status,delivery_attempts
-- )
ALTER TABLE locations 
ALTER COLUMN location_id SET NOT NULL ,
ALTER COLUMN city SET NOT NULL ,
ALTER COLUMN region SET NOT NULL ;

--warehouses.csv (warhouse_id,warehouse_name,location_id,capacity)
ALTER TABLE warehouses 
ALTER COLUMN warehouse_id SET NOT NULL,
ALTER COLUMN warehouse_name SET NOT NULL ,
ALTER COLUMN location_id SET NOT NULL ,
ALTER COLUMN capacity SET NOT NULL ;

-- delivery_partners.csv (partner_id,partner_name)
ALTER TABLE delivery_partners
ALTER COLUMN partner_id SET NOT NULL ,
ALTER COLUMN partner_name SET NOT NULL ;

--customers.csv (c_id,c_name,city,region,c_type)
ALTER TABLE customers 
ALTER COLUMN c_id SET NOT NULL , 
ALTER COLUMN c_name SET NOT NULL,
ALTER COLUMN city SET NOT NULL,
ALTER COLUMN region SET NOT NULL,
ALTER COLUMN c_type SET NOT NULL ;


-- orders.csv (o_id,c_id,warhouse_id,destination_location_id,o_date,o_value,priority) 
ALTER TABLE orders 
ALTER COLUMN o_id SET NOT NULL,
ALTER COLUMN c_id SET NOT NULL,
ALTER COLUMN warehouse_id SET NOT NULL,
ALTER COLUMN destination_location_id SET NOT NULL,
ALTER COLUMN o_date SET NOT NULL,
ALTER COLUMN o_value SET NOT NULL,
ALTER COLUMN priority SET NOT NULL ; 

-- --shipments.csv (shipment_id,o_id,partner_id,dispatch_date,expected_delivery_date,actual_delivery_date,status,delivery_attempts
-- )
ALTER TABLE shipments 
ALTER COLUMN shipment_id SET NOT NULL , 
ALTER COLUMN o_id SET NOT NULL ,
ALTER COLUMN partner_id SET NOT NULL ,
ALTER COLUMN dispatch_date SET NOT NULL ,
ALTER COLUMN expected_delivery_date SET NOT NULL ,
ALTER COLUMN actual_delivery_date SET NOT NULL ,
ALTER COLUMN status SET NOT NULL ,
ALTER COLUMN delivery_attempts SET NOT NULL ;



-- CHECK CONSTRAINTS 

-- locations.csv (location_id,city,region)
--warhouses.csv (warhouse_id,warehouse_name,location_id,capacity)
-- delivery_partners.csv (partner_id,partner_name)
--customers.csv (c_id,c_name,city,region,c_type)
-- orders.csv (o_id,c_id,warhouse_id,destination_location_id,o_date,o_value,priority) 
-- --shipments.csv (shipment_id,o_id,partner_id,dispatch_date,expected_delivery_date,actual_delivery_date,status,delivery_attempts

ALTER TABLE warehouses 
ADD CONSTRAINT chk_warehouse_capacity 
CHECK (capacity > 0) ;

ALTER TABLE orders 
ADD CONSTRAINT chk_order_value 
CHECK (o_value >= 0) ; 

ALTER TABLE shipments 
ADD CONSTRAINT chk_shipment_attempts 
CHECK (delivery_attempts >= 0) ;

ALTER TABLE shipments 
ADD CONSTRAINT chk_shipment_status 
CHECK (status IN ('Delivered', 'Delayed')) ;

ALTER TABLE orders 
ADD CONSTRAINT chk_order_priority 
CHECK (priority IN ('Standard', 'Express')) ;

