import streamlit as st
import pandas as pd
from PIL import Image

PAGE_CONFIG = {"page_title": "Simple Data Dashboard",
               "layout": "centered",
               "initial_sidebar_state": "auto"}

st.set_page_config(**PAGE_CONFIG)

st.title("Simple Data Dashboard")

upload_file = st.file_uploader("Choose a csv file", type="csv")

if upload_file is not None:
    df = pd.read_csv(upload_file)

    st.header("Data Preview")
    st.write(df.head())

    st.header("Data Summary")
    st.write(df.describe())

    st.header("Filter Data")
    columns = df.columns.tolist()
    selected_columns = st.selectbox("Select column to filter by", columns)
    unique_values = df[selected_columns].unique()
    selected_values = st.selectbox("Select Value", unique_values)

    filtered_df = df[df[selected_columns] == selected_values]
    st.write(filtered_df)

    st.header("Plot Data")
    x_column = st.selectbox("Select x-axis column", columns)
    y_column = st.selectbox("Select y-axis column", columns)

    if st.button("Generate Plot"):
        st.line_chart(filtered_df.set_index(x_column)[y_column])

else:
    st.write("Waiting for file upload...")
