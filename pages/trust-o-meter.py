#import functions
import streamlit as st
import plotly.graph_objects as go
#from langchain.llms import OpenAI
#from PIL import Image

from layout_template import sidebar_template

PAGE = "🌡️ Government Trust-O-Meter"
PROMPT = ''

answer, docs = '', []
# -------------------- Sidebar Layout --------------------
sidebar_template()

# -------------------- Page Header --------------------
st.header(PAGE, divider=True)

# -------------------- Container --------------------
container = st.container(border=True)
container.subheader("Overall, how much do you trust \"government\"?", divider=None)

# Create a slider to select a value
selected_value = container.slider("0 = None / 100 = Full", min_value=0, max_value=100, value=50)

# Create a gauge/dial using Plotly
fig = go.Figure(go.Indicator(
    mode="gauge+number",
    value=selected_value,
    gauge={'axis': {'range': [0, 100]},
            'bar': {'color': "blue"},
            'steps': [
               {'range': [0 , 25], 'color': "red"},
               {'range': [25, 40], 'color': "orangered"},
               {'range': [40, 55], 'color': "orange"},
               {'range': [55, 70], 'color': "yellow"},
               {'range': [70, 85], 'color': "yellowgreen"},
               {'range': [85, 100], 'color': "green"}
            ]},
    title={'text': "Trust Gauge (city, state, federal)"},
))

# Display the gauge in Streamlit
container.plotly_chart(fig)

selected_value = container.slider("How much do you trust your **CITY** government?", min_value=0, max_value=100, value=50)
selected_value = container.slider("How much do you trust your **STATE** government?", min_value=0, max_value=100, value=50)
selected_value = container.slider("How much do you trust your **FEDERAL** government?", min_value=0, max_value=100, value=50)

# -------------------- Container --------------------
suggestions = st.container(border=True)
suggestions.subheader("Suggestion Box", divider="gray")

suggestions.text_area("What's _one thing_  civic leaders can do better?", max_chars=200, placeholder="Our leaders should...")

st.button("Submit my feedback", type="secondary")
