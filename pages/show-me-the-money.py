import pdb
import functions
import streamlit as st
from functions import logUserFeedback, generatePrediction
from layout_template import sidebar_template, render_radio

PAGE = "💵 Show Me The Money!"

# -------------------- Sidebar Layout --------------------
sidebar_template()

# -------------------- Page Header --------------------
st.header(PAGE, divider=True)

st.markdown("""
#### Every proposition has costs -- both overt and hidden.  This page using generative AI to ferret out the costs of each proposed measure.
""")

# -------------------- Page Body --------------------
render_radio()

# -------------------- Output --------------------
with st.container(border=True):
  if st.button("Generate!"):
    USER_PROMPT = f"Break down, in as much detail as you can, the total cost of this proposal.  If possible, break-out cost per tax payer, lifetime cost of the measure and financing fees."
    PROPOSITION = st.session_state.selected_prop

    with st.spinner(f'Generating {PAGE} summary for *{PROPOSITION.split("-")[0].strip()}*...'):
      st.markdown(generatePrediction(PROPOSITION, USER_PROMPT))

# -------------------- Feedback --------------------
feedback_button = st.feedback("thumbs")
if feedback_button is not None:
  logUserFeedback(f"{PAGE}: feedback= {'+1' if feedback_button == 1 else '-1'}")