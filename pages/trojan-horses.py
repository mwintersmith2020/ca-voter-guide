import functions
import streamlit as st
from functions import logUserFeedback, generatePrediction
from layout_template import sidebar_template, render_radio


PAGE = "🐴 Trojan Horses"

# -------------------- Sidebar Layout --------------------
sidebar_template()

# -------------------- Page Header --------------------
st.header(PAGE, divider=True)

st.markdown(f"""
### **Greetings, Voter {st.session_state.name}!**

##### Use this page to identify any hidden provisions ("riders") buried deep in the proposal's text.
""")

# -------------------- Page Body --------------------
render_radio()

# -------------------- Output --------------------
with st.container(border=True):
  if st.button("Generate!"):
    USER_PROMPT = f"Please describe any hidden or otherwise obfuscated details of this proposal.  Please also describe any unintendeed consequences of this proposal."
    PROPOSITION = st.session_state.selected_prop

    with st.spinner(f'Generating {PAGE} summary for *{PROPOSITION.split("-")[0].strip()}*...'):
      st.markdown(generatePrediction(PROPOSITION, USER_PROMPT))

# -------------------- Feedback --------------------
feedback_button = st.feedback("thumbs")
if feedback_button is not None:
  logUserFeedback(f"{PAGE}: feedback= {'+1' if feedback_button == 1 else '-1'}")