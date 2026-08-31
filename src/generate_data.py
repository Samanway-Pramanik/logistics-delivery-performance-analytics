import csv
import random 
from datetime import datetime , timedelta 
import os 

print("generating logistics data : ") 

# Find project root
PROJECT_ROOT = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)

OUTPUT_DIR = os.path.join(
    PROJECT_ROOT,
    "data",
    "raw"
)

os.makedirs(OUTPUT_DIR, exist_ok=True)

random.seed(42)

# Datas that I am wanting to use randomly 
cities = [
    "Bangalore", 
    "Mumbai" ,
    "Delhi",
    "Hyderabad" ,
    "Pune" ,
    "Chenni",
    "Kolkata" 
]

regions = {
    "Bangalore" : "South" ,
    "Mumbai" : "West" ,
    "Delhi" : "North" ,
    "Hyderabad" : "South" ,
    "Pune" : "West" ,
    "Chenni" : "South" ,
    "Kolkata" : "East" 
}

first_names = [
    "Samanway", "Sameer" , "Rahul", "Sneha", "Anushka" , "Anjali" , "Amrita" , "Rohit" , "Surya" , "Vikram" , "karan", "Preetam" , "Saurabh" , "Vansh", "Siddharth" 
]

last_names = [
    "Pramanik", "Kumar", "Gupta" , "Roy" , "Modi" , "Das" , "Senapati" , "Singh" , "Sharma" , "Shah" , "Chaturvedi" , "Mishra" , "Sahi" , "Dey" , "Shome"
]

priorities = [
    "Standard" ,
    "Standard" , 
    "Standard" , 
    "Express"
]

statuses = [
    "Delivered" ,
    "Delivered" , 
    "Delivered" ,
    "Delivered" ,
    "Delayed"
]

# Locations ---------- location_id , city, region
locations_file = os.path.join(
    OUTPUT_DIR, 
    "locations.csv"
)

with open(locations_file, "w" , newline="" ) as file :
    writer = csv.writer(file) 
    
    writer.writerow (
        [
            "location_id" ,
            "city" ,
            "region"
        ]
    ) 
    for i, city in enumerate(cities, start = 1) :
        writer.writerow(
            [
                i, 
                city,
                regions[city]
            ]
        )
        
        

# warehouses.csv ---------> warhouse_id, w_name, location-id , capacity
warehouse_file = os.path.join(
    OUTPUT_DIR,
    "warehouses.csv" 
)

with open (warehouse_file, "w" , newline="") as file :
    writer = csv.writer(file) 
    
    writer.writerow(
        [
            "warehouse_id" ,
            "warehouse_name" ,
            "location_id" ,
            "capacity" 
        ]
    )
    
    for i in range(1,6) :
        writer.writerow(
            [
                i, 
                f"warehouse {chr(64+i)}" ,
                random.randint(1,7) ,
                random.randint(1000, 3000) 
            ]
        )
        

# delivery_parteners.csv  ------> partner_id, partner_name 
partner_file = os.path.join(
    OUTPUT_DIR,
    "delivery_partners.csv" 
)

with open(partner_file , "w" , newline="" ) as file :
    writer = csv.writer(file) 
    
    writer.writerow (
        [
            "partner_id" , 
            "partner_name"
        ]
    )
    
    partner_names = [
        "FastTrack" ,
        "SwiftShip" ,
        "QuickMove" ,
        "ParcelPro",
        "CityRunner"
    ] 
    
    for i, name in enumerate(partner_names , start =1 ) :
        writer.writerow(
            [
                i, 
                name
            ]
        )
        
        

# customers.csv -----> c_id, c_name, city, region, c_type
customers_file = os.path.join(
    OUTPUT_DIR,
    "customers.csv" 
)

with open(customers_file, "w" , newline="") as file :
    writer = csv.writer(file) 
    
    writer.writerow(
        [
            "c_id",
            "c_name" ,
            "city" ,
            "region" ,
            "c_type" 
        ]  
    )
    customer_types = [
        "Regular" ,
        "Regular" ,
        "Regular" ,
        "Premium" ,
        "Business"
    ] 
    
    for i in range(1, 501) :
        name = (
            f"{random.choice(first_names)} "
            f"{random.choice(last_names)}"
        )    
        city = random.choice(cities) 
        c_type = random.choice(customer_types)
        
        writer.writerow(
            [
                i, 
                name, 
                city,
                regions[city] ,
                c_type
            ]
        )


# orders.csv-----> o_id, c_id, warehouse_id, destination_location_id, o_date, o_value,priority 
orders_file = os.path.join(
    OUTPUT_DIR,
    "orders.csv"
)
start_date = datetime(2025, 1, 1)
with open (orders_file, "w", newline="") as file:
    writer = csv.writer(file) 
    
    writer.writerow(
        [
            "o_id" , 
            "c_id" , 
            "warehouse_id" ,
            "destination_location_id" , 
            "o_date" , 
            "o_value" , 
            "priority" 
        ]
    )
    
    for i in range(1, 4001) :
        
        order_date = (
            start_date + timedelta(days = random.randint(0, 364))
        )
        
        c_id = random.randint(1, 500)  # inclusive  => []
        warehouse_id = random.randint(1,5) 
        destination_location_id = random.randint(1, 7) 
        o_date = order_date.strftime("%Y-%m-%d") 
        o_value = round(random.uniform(300, 1500), 2) 
        priority = random.choice(priorities)
        
        writer.writerow(
            [
                i, 
                c_id, 
                warehouse_id,
                destination_location_id,
                o_date,
                o_value, 
                priority
            ]
        )
        
        
# shipments.csv ----> shipment_id, o_id, partner_id, dispatch_date, expected-delivery_date ,actual_delivery_date, status, delivery_attempts 

delivery_file = os.path.join(
    OUTPUT_DIR, 
    "shipments.csv"
)

with open(delivery_file, "w", newline="") as file:
    writer = csv.writer(file) 
    
    writer.writerow(
        [
            "shipment_id" , 
            "o_id" , 
            "partner_id" ,
            "dispatch_date" , 
            "expected_delivery_date" , 
            "actual_delivery_date" , 
            "status" ,
            "delivery_attempts" 
        ]
    )
    
    for i in range(1, 4001) : 
        
        # for every order, one shipment , so o_id == shipment_id
        partner_id = random.randint(1,5)  # 5 total partnerrs are there 
        
        dispatch_date_not_str = (
            start_date + timedelta(days = random.randint(0,364))
        ) 
        dispatch_date = dispatch_date_not_str.strftime("%Y-%m-%d") 
        
        
        expected_days_to_deliver = random.randint(2,5)  #date of delivery from dispatch date 
        expected_delivery_date_not_str = (
            dispatch_date_not_str + timedelta(days = expected_days_to_deliver) 
        )
        expected_delivery_date = expected_delivery_date_not_str.strftime("%Y-%m-%d") 
        
        status = random.choice(statuses)
        
        # actual_delivery_date 
        if status == "Delayed" :
            actual_delivery_date_not_str = (
                expected_delivery_date_not_str + timedelta(days = random.randint(1,4))
            )
            
            actual_delivery_date = actual_delivery_date_not_str.strftime("%Y-%m-%d")
            
        else :
            actual_delivery_date = expected_delivery_date
        
        delivery_attempts = random.randint(1,3)  # inclusive => []
        
        writer.writerow(
            [
                i, 
                i,
                partner_id, 
                dispatch_date, 
                expected_delivery_date, 
                actual_delivery_date, 
                status, 
                delivery_attempts
            ]
        )
        

# -----------------
print(f"Data Generation completed ! ") 

print(
    f"created files : \n\n" 
    f"customers.csv \n"
    f"locations.csv \n" 
    f"warehouses.csv\n" 
    f"delivery_partners.csv \n"
    f"orders.csv \n" 
    f"shipments.csv" 
)

print(f"Location : {OUTPUT_DIR}")
        