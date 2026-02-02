import streamlit as st

st.title("Chai Maker App")

# if st.button("Make Chai"):
#     st.success("Your chai is ready!")

current_year = 2026
date = st.date_input("Select a date")

cal_year = current_year - date.year

if st.button("Calculate Age"):
    if cal_year < 0:
        st.error("You are not born yet")
    elif cal_year == 0:
        st.warning("You are a new born")
    else:
        st.success(f"Your age is {cal_year}")
# st.write(f"Your age is {cal_year}")