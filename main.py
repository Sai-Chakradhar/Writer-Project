import streamlit as st

# Sidebar navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Page 1", "Page 2"])

if page == "Page 1":
    import home
    home.app()
elif page == "Page 2":
    import page2
    page2.app()