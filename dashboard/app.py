import streamlit as st
import pandas as pd

from db_connection import get_connection
import queries

# Page setup
st.set_page_config(
    page_title="Logistics Analytics",
    layout="wide"
)

st.title("Logistics & Delivery Performance Analytics")

st.write(
    "SQL-based analysis of logistics and delivery operations."
)


# Database connection
connection = get_connection()

#Helper function
def get_data(query):
    return pd.read_sql(query, connection)


# ---------------------------------------------------------
# KPI section
# ---------------------------------------------------------

total_orders = get_data(
    queries.TOTAL_ORDERS
).iloc[0]["total_orders"]

total_shipments = get_data(
    queries.TOTAL_SHIPMENTS
).iloc[0]["total_shipments"]


col1, col2 = st.columns(2)

with col1:
    st.metric("Total Orders", total_orders)

with col2:
    st.metric("Total Shipments", total_shipments)


# Shipment Status
st.subheader("Shipment Status")

status_data = get_data(
    queries.SHIPMENT_STATUS
)

st.bar_chart(
    status_data.set_index("status")
)


# Orders by Warehouse
st.subheader("Orders by Warehouse")

warehouse_data = get_data(
    queries.ORDERS_BY_WAREHOUSE
)

st.bar_chart(
    warehouse_data.set_index("warehouse_name")
)



# Orders by City
st.subheader("Orders by Destination City")

city_data = get_data(
    queries.ORDERS_BY_CITY
)

st.bar_chart(
    city_data.set_index("city")
)


# Delivery Partner Performance
st.subheader("Shipments by Delivery Partner")

partner_data = get_data(
    queries.PARTNER_PERFORMANCE
)

st.bar_chart(
    partner_data.set_index("partner_name")
)


connection.close()