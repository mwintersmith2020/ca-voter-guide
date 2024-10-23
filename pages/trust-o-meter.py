import functions
import streamlit as st
import plotly.graph_objects as go
#from langchain.llms import OpenAI
#from PIL import Image

from layout_template import sidebar_template
from functions import logUserFeedback

PAGE = "🌡️ Government Trust-O-Meter"

# -------------------- Sidebar Layout --------------------
sidebar_template()

# -------------------- Page Header --------------------
st.header(PAGE, divider=True)

# -------------------- Container --------------------
container = st.container(border=True)
container.subheader(f"Overall, {st.session_state.name} how much do you trust \"government\"?", divider=None)

# Create a slider to select a value
overall_value = container.slider("0 = Not at all / 100 = Complete trust", min_value=0, max_value=100, value=50)

# Create a gauge/dial using Plotly
fig = go.Figure(go.Indicator(
    mode="gauge+number",
    value=overall_value,
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

city_value = container.slider("How much do you trust your **CITY** government?", min_value=0, max_value=100, value=50)
state_value = container.slider("How much do you trust your **STATE** government?", min_value=0, max_value=100, value=50)
federal_value = container.slider("How much do you trust your **FEDERAL** government?", min_value=0, max_value=100, value=50)

# -------------------- Container --------------------
suggestions = st.container(border=True)
suggestions.subheader("Suggestion Box", divider="gray")

feedback = suggestions.text_area("What's _one thing_  civic leaders can do better?", max_chars=200, placeholder="Our leaders should...")

if st.button("Submit my feedback", type="secondary"):
    logUserFeedback(f"{PAGE}: overall= {overall_value}, city= {city_value}, state= {state_value}, federal= {federal_value}")
    logUserFeedback(f"{PAGE}: feedback= {feedback}")
    st.success("Feedback submitted successfully!")
