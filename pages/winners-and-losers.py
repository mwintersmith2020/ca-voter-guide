import pdb
import functions
import streamlit as st
from functions import logUserFeedback, generatePrediction
from layout_template import sidebar_template, render_radio

PAGE = "🎲 Winners & Losers"

# -------------------- Sidebar Layout --------------------
sidebar_template()

# -------------------- Page Header --------------------
st.header(PAGE, divider=True)

st.markdown("""
#### Every proposed new legislation has winners and losers.  This page uses generative AI to determine (as best it can) who the winners and losers are for the propositions on the November ballot.
""")
# -------------------- Page Body --------------------
render_radio()

# -------------------- Output --------------------
with st.container(border=True):
  if st.button("Generate!"):
    USER_PROMPT = f"Create a section called WINNERS and write a bulleted list of who wins with this proposition.  Create another called LOSERS and write a bulleted list of who loses with this proposition."
    PROPOSITION = st.session_state.selected_prop

    with st.spinner(f'Generating {PAGE} summary for *{PROPOSITION.split("-")[0].strip()}*...'):
      st.markdown(generatePrediction(PROPOSITION, USER_PROMPT))

# -------------------- Feedback --------------------
feedback_button = st.feedback("thumbs")
if feedback_button is not None:
  logUserFeedback(f"{PAGE}: feedback= {'+1' if feedback_button == 1 else '-1'}")
