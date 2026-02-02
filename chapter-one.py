import streamlit as st

st.title("Hello, World!")
st.subheader("This is a subheader")
st.text("This is some text")

st.write("Choose your fav programming language")
lang = st.selectbox("Programming Language", ["Python", "Java", "C++", "JavaScript"])
st.write(f"Your fav language is {lang}")
st.success(f"You have selected {lang} as your fav language")