import streamlit as st

#sets the page to wide layout which is not automatic
st.set_page_config(layout = 'wide')

st.title("My Card Collector App")

if st.button("Click Me"):
    st.write("👋 Hi")
