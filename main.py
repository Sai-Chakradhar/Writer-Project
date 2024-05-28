import streamlit as st

# Sidebar navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Text Generation", "Text Rewriter"])

if page == "Text Generation":
    import home
    home.app()
elif page == "Text Rewriter":
    import page2
    page2.app()