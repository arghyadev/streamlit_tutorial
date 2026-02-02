import streamlit as st

st.title("Chai Taste Poll")

col1, col2 = st.columns(2)

with col1:
    st.header("Masal Chai")
    st.image("https://images.pexels.com/photos/26873298/pexels-photo-26873298.jpeg", width=200)
    vote1 = st.button("Vote for Masal Chai")

with col2:
    st.header("Adrak Chai")
    st.image("https://images.pexels.com/photos/33104714/pexels-photo-33104714.jpeg", width=200)
    vote2 = st.button("Vote for Adrak Chai")

if vote1:
    st.success("You voted for Masal Chai")
elif vote2:
    st.success("You voted for Adrak Chai")


with st.expander("View Results"):
    st.write("""
    # Chai Taste Poll Results
    ## Masal Chai
    - 50%

    ## Adrak Chai
    - 50%
    """
    )