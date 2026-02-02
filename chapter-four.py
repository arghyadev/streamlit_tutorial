import streamlit as st
import pandas as pd

st.title("Chai Sales Dashboard")

file = st.file_uploader("Upload a CSV file", type=["csv"])
if file:
    df = pd.read_csv(file)
    st.subheader("Data Preview")
    st.dataframe(df)
    # st.line_chart(df, x="Date", y="Revenue")

if file:
    cities = df["City"].unique()
    st.subheader("Select a City")
    selected_city = st.selectbox("City", cities)
    filtered_df = df[df["City"] == selected_city]
    st.dataframe(filtered_df)

    st.subheader("Chai Sales Analysis")
    st.bar_chart(filtered_df, x="Chai_Type", y="Revenue")