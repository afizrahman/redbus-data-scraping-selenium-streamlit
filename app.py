import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
st.title("Redbus Data")
import streamlit as st
import pandas as pd
import os

# ----------- 1. Path to inner Redbus_data folder -----------
data_folder = r"C:\Users\USER\OneDrive\Desktop\red bus\Redbus_data\Redbus_data"

# ----------- 2. Load all CSV files -----------
csv_files = [f for f in os.listdir(data_folder) if f.endswith('.csv')]

if not csv_files:
    st.error(" No CSV files found in Redbus_data folder")
else:
    df_list = [pd.read_csv(os.path.join(data_folder, f)) for f in csv_files]
    df = pd.concat(df_list, ignore_index=True)

    # ----------- 3. Streamlit Dashboard -----------
    st.title("Redbus Data Dashboard")
    st.subheader("All Bus Details")

    # ----------- 4. Filters -----------

    # Filter by Route Name
    if 'Route Name' in df.columns:
        route_options = df['Route Name'].unique().tolist()
        selected_route = st.multiselect("Select Route(s):", options=route_options, default=route_options)
    else:
        selected_route = df['Route Name']

    # Filter by Bus Type
    if 'Bus Type' in df.columns:
        bus_type_options = df['Bus Type'].unique().tolist()
        selected_bus_type = st.multiselect("Select Bus Type(s):", options=bus_type_options, default=bus_type_options)
    else:
        selected_bus_type = df['Bus Type']

    # Filter by Price Range
    if 'Price' in df.columns:
        min_price = int(df['Price'].min())
        max_price = int(df['Price'].max())
        selected_price = st.slider("Select Price Range", min_price, max_price, (min_price, max_price))
    else:
        selected_price = (df['Price'].min(), df['Price'].max())

    # ----------- 5. Apply all filters together -----------
    filtered_df = df[
        df['Route Name'].isin(selected_route) &
        df['Bus Type'].isin(selected_bus_type) &
        df['Price'].between(selected_price[0], selected_price[1])
    ]

    st.subheader(f"Filtered Buses ({len(filtered_df)} results)")
    st.dataframe(filtered_df)






