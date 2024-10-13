# layout_template.py

import streamlit as st
from PIL import Image

BOOK_IMAGE = Image.open("img/ca-voter-guide.png")

def sidebar_template():
    # Sidebar
    # st.sidebar.title("Navigation")
    # st.sidebar.write("This is a shared sidebar for all pages.")
    st.sidebar.image(BOOK_IMAGE)
    st.sidebar.markdown("---")

    st.sidebar.page_link("pages/user-agent.py", label="<User Agent>")

    st.sidebar.page_link("pages/trust-o-meter.py", label="Trust-O-Meter")
    st.sidebar.page_link("pages/winners-and-losers.py", label="Winners & Losers")
    st.sidebar.page_link("pages/show-me-the-money.py", label="Show Me The Money!")
