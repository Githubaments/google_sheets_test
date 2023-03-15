import streamlit as st
from gsheetsdb import connect

# Connect to Google Sheets
conn = connect()

# Query the specific sheet by name
query = "SELECT * FROM `Form responses 2$`"

# Execute the query and read the results into a pandas dataframe
df = conn.execute(query).fetch_data()

# Display the dataframe in Streamlit
st.dataframe(df)
