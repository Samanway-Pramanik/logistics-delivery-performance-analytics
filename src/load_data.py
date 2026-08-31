import csv 
import os 
import psycopg2 
from dotenv import load_dotenv 

# loading database credentials 
load_dotenv () 

DB_HOST = os.getenv("DB_HOST") 
DB_PORT = os.getenv("DB_PORT") 
# DB_NAME = os.getenv("DB_NAME") 
DB_USER = os.getenv("DB_USER") 
DB_PASSWORD = os.getenv("DB_PASSWORD") 

DB_NAME = "logistics_analytics" 

# project path 
PROJECT_ROOT = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)

DATA_DIR = os.path.join(
    PROJECT_ROOT,
    "data",
    "raw" 
)

DATABASE_DIR = os.path.join(
    PROJECT_ROOT,
    "database"
)


# CReate the databse if not exists 
connection = psycopg2.connect(
    host = DB_HOST ,
    port = DB_PORT ,
    database = "postgres" ,
    user = DB_USER ,
    password = DB_PASSWORD       
)

connection.autocommit = True 

cursor = connection.cursor() 

cursor.execute(
    "SELECT 1 FROM pg_database WHERE datname = %s",
    (DB_NAME,) 
)

if cursor.fetchone() :
    print(f"Database : {DB_NAME} already exists .") 
else :
    cursor.execute(
        f"CREATE DATABASE {DB_NAME}"
    )
    print(f"Database : {DB_NAME} created. ") 
    
    
cursor.close() 
connection.close() 


# Noe connecting to the project database (that we just created above) 
connection = psycopg2.connect(
    host = DB_HOST,
    port = DB_PORT , 
    database = DB_NAME ,
    user = DB_USER ,
    password = DB_PASSWORD 
)
cursor = connection.cursor() 
print("Connected to the project database : logistics_analytics .") 

 
 
# cretae tables 

create_tables_path = os.path.join(
    DATABASE_DIR,
    "01_create_tables.sql"
)

with open (create_tables_path , "r") as file :
    create_tables_sql = file.read() 
    
cursor.execute(create_tables_sql) 
print("Tabkles created successfully ! ") 

# ADD constarints 
constraints_path = os.path.join(
    DATABASE_DIR,
    "02_constraints.sql"
)

with open (constraints_path , "r") as file :
    constraints_sql = file.read()

cursor.execute(constraints_sql) 
print("Constraints added successfuly .") 



# csv files and corresponding tables 
files_and_tables = [
    ("locations.csv", "locations") ,
    ("warehouses.csv", "warehouses"),
    ("delivery_partners.csv", "delivery_partners") ,
    ("customers.csv", "customers") ,
    ("orders.csv", "orders") ,
    ("shipments.csv" , "shipments")
]

# loading csv datas 

for filename , table_name in files_and_tables :
    file_path = os.path.join(
        DATA_DIR,
        filename 
    )
    
    with open(file_path , "r" , newline="" ) as file :
        reader = csv.reader(file) 
        
        next(reader)  # skiping the header row (the col names ) 
        
        for row in reader :
            placeholders = ", ".join(
                ["%s"] * len(row)
            )
            query = f"""
                INSERT INTO {table_name} 
                VALUES ({placeholders})
            """
            
            cursor.execute(query, row) 
    
    print(f" {filename} loaded to {table_name}") 
    

# saveing changes 
connection.commit() 

print("\n All data has been loaded successfully !!!! ") 


cursor.close() 
connection.close() 

print("Postgresql comnnection closed ! ")
            
            
            
            
            
