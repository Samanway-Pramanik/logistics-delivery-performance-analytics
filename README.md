# Logistics & Delivery Performance Analytics

An end-to-end data analytics project that explores logistics and delivery operations using Python, PostgreSQL, SQL, and Streamlit. The project organizes logistics data into a relational database, performs SQL-based operational analysis, and presents key metrics and findings through an interactive dashboard.

## Project Overview

Logistics teams need to monitor delivery performance, understand delays, compare operational segments, and identify where performance needs attention. This project uses a structured logistics dataset to examine delivery and shipment patterns and turn the analysis into accessible dashboard insights.

The workflow covers data generation, database setup, loading CSV data into PostgreSQL, SQL analysis, and dashboard presentation.

## Objectives

- Organize logistics entities and operational records into a relational database.
- Prepare and load CSV datasets into PostgreSQL.
- Use SQL to analyze delivery performance and operational trends.
- Examine metrics across relevant dimensions such as delivery partners, warehouses, locations, customers, orders, and shipments.
- Present selected KPIs and analysis in an interactive Streamlit dashboard.

## Tech Stack

| Technology | Use |
|---|---|
| Python | Data generation, loading scripts, application logic |
| PostgreSQL | Relational database and analytical queries |
| SQL | Schema definition, constraints, joins, aggregations, and analysis |
| Psycopg2 / PostgreSQL Python connectivity | Connect Python scripts to the database |
| Streamlit | Interactive dashboard interface |
| Pandas | Data handling for dashboard presentation |
| CSV | Source data files |
| Git & GitHub | Version control and project hosting |

## Data Model

The project uses CSV files representing these logistics entities:

- **Customers** — customer records
- **Orders** — order information
- **Shipments** — shipment and delivery records
- **Warehouses** — warehouse information
- **Delivery Partners** — delivery service/partner records
- **Locations** — location-related records

The database schema and constraints are defined in SQL scripts. Relationships between the entities allow the analysis to combine operational data across tables instead of treating each CSV as an isolated file.

## Project Workflow

```text
CSV Source Data
      ↓
Python Data Generation / Preparation
      ↓
PostgreSQL Schema & Constraints
      ↓
Python Data Loading
      ↓
Relational Database
      ↓
SQL Analysis Queries
      ↓
KPI / Operational Insights
      ↓
Streamlit Dashboard
```

## Repository Structure

```text
logistics-delivery-performance-analytics/
├── dashboard/
│   ├── app.py                 # Streamlit dashboard entry point
│   ├── db_connection.py        # Database connection utilities
│   └── queries.py              # Dashboard SQL queries
├── data/
│   └── raw/
│       ├── customers.csv
│       ├── delivery_partners.csv
│       ├── locations.csv
│       ├── orders.csv
│       ├── shipments.csv
│       └── warehouses.csv
├── database/
│   ├── 01_create_tables.sql    # Table creation / schema
│   └── 02_constraints.sql      # Constraints and relationships
├── screenshots/                 # Dashboard screenshots (if included)
├── sql/
│   └── 03_analysis_queries.sql # Analytical SQL queries
├── src/
│   ├── generate_data.py        # Data generation script
│   ├── load_data.py            # CSV-to-database loading script
│   └── utils.py                # Shared helper functions
├── .env                        # Local credentials (not committed)
├── .env.example                 # Example environment configuration
├── .gitignore
├── README.md
└── requirements.txt
```

> Folder names and file paths above reflect the project layout shown in the repository screenshots. Adjust any path if it has changed in the current branch.


## Setup & Run

### 1. Clone the repository

```bash
git clone https://github.com/Samanway-Pramanik/logistics-delivery-performance-analytics.git
cd logistics-delivery-performance-analytics
```

### 2. Create and activate a Python environment

```bash
python -m venv .venv
```

**Linux / macOS**

```bash
source .venv/bin/activate
```

**Windows (PowerShell)**

```powershell
.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure PostgreSQL credentials

Create a local `.env` file using `.env.example` as a template. Set the connection values to match your PostgreSQL installation and database.

Example configuration (use the variable names expected by the project code):

```env
DB_HOST=localhost
DB_PORT=5432
DB_NAME=logistics_db
DB_USER=postgres
DB_PASSWORD=your_password
```

Do not commit real passwords or credentials. The variable names above are illustrative; use the names defined in the project's connection code if they differ.

### 5. Create the database and tables

Create the PostgreSQL database (for example, `logistics_db`) using pgAdmin or `psql`. Then run the schema scripts in order:

```bash
psql -d logistics_db -f database/01_create_tables.sql
psql -d logistics_db -f database/02_constraints.sql
```

If your local setup requires explicit connection parameters, add them to your `psql` command or configure your PostgreSQL connection first.

### 6. Generate / prepare the source CSV data

Run the data-generation script if you want to recreate the project's CSV data:

```bash
python src/generate_data.py
```

Review the script's output path before running if you want the generated files to replace the existing CSVs.

### 7. Load CSV data into PostgreSQL

After the database schema is created and the CSV data is available, run:

```bash
python src/load_data.py
```

The loader uses the project's database connection configuration to insert data into PostgreSQL. Run it only after verifying that the database and tables are set up.

### 8. Run SQL analysis

Execute the analytical queries in:


```text
sql/03_analysis_queries.sql
```

These queries are intended for exploring delivery and logistics metrics across the connected tables.

### 9. Launch the Streamlit dashboard

```bash
streamlit run dashboard/app.py
```

Streamlit will print a local URL in the terminal (usually `http://localhost:8501` or `http://localhost:8501` depending on configuration). Open that address in your browser to interact with the dashboard.

## Analysis Areas

The SQL analysis and dashboard are intended to explore operational performance through questions such as:


- How are orders and shipments distributed across the dataset?
- How do delivery partners compare across shipment volume and performance metrics?
- What patterns appear across warehouses and locations?
- Which operational segments show signs of weaker delivery performance?
- How do delivery-related measures vary across time or groups, where the available fields support such analysis?

The precise metrics and conclusions depend on the queries and fields present in the project data.

## Dashboard

The Streamlit dashboard provides a user-facing view of selected logistics metrics and SQL-based analysis. It is connected to PostgreSQL through the dashboard's connection module, while dashboard queries are organized separately to keep database access and query logic distinct from the main UI code.


> Add dashboard screenshots here once available, for example: `![Dashboard overview](screenshots/dashboard_overview.png)`

## Database & SQL Concepts

The project demonstrates practical relational database and SQL work, including:

- Relational tables and entity relationships
- Primary and foreign keys / integrity constraints (as defined in the SQL scripts)
- Multi-table joins
- Aggregation and grouping
- Filtering and conditional analysis
- KPI-oriented queries

Additional SQL techniques should be listed here only if they are present in `03_analysis_queries.sql`.

## Notes & Limitations

- This is an analytics project built around the available dataset; it is not a live logistics tracking system.
- The dashboard reports patterns in the data and does not itself prove that operational changes would improve delivery outcomes.
- Dataset size, KPI definitions, and specific findings should be documented using the actual generated data and analysis outputs rather than assumed values.

## Future Improvements

- Add dashboard filters for more operational dimensions.
- Add data validation checks to the loading workflow.
- Improve logging and error reporting in the data-loading script.
- Automate refresh and data-loading steps.
- Expand the analysis with additional KPIs as new data fields become available.

## Author

**Samanway Pramanik**

GitHub: [Samanway-Pramanik](https://github.com/Samanway-Pramanik)
