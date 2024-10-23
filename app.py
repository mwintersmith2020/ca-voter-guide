import re
import time
import functions
import streamlit as st
from functions import logUserFeedback, generatePrediction
from layout_template import sidebar_template, render_radio

# -------------------- Initialization --------------------

# NOTE: streamlit.errors.StreamlitSetPageConfigMustBeFirstCommandError:
#  `set_page_config()` can only be called once per app page, and must be called as the first 
# Streamlit command in your script.

#st.set_page_config(layout="wide")

# NOTE: streamlit.errors.StreamlitAPIException: logger.level cannot be set on the fly. 
# Set as command line option, e.g. streamlit run script.py --logger.level, or in config.toml instead.
# DOESN'T WORK --> st.set_option('logger.level', 'INFO')


PAGE = "🗳️ Summary of Propositions"
age_level = '8th-grader'

# ---------------------- Sidebar ----------------------

sidebar_template()

# -------------------- Page Header --------------------
st.header(PAGE, divider=True)

st.markdown(f"""
### **Greetings, Voter {st.session_state.name}!**

#### Generative A.I. can help demystify the voting process by providing interative tools which allow you to ask questions in plain English.
""")

# -------------------- Page Body --------------------
render_radio()

# -------------------- Output --------------------
with st.container(border=True):

  age_level = st.select_slider(
    "Sophistication level:",
    options=[
        "4th-grader",
        "8th-grader",
        "High school student",
        "Ph.D. candidate",
        "Lawyer",
    ],
    value="High school student",
  )

  if st.button(f"Summarize this proposition for a **{age_level}**:"):
    USER_PROMPT = f"Please summarize this proposition in 5 bullet points (or less) for a {age_level}, using the vocabulary and speech suitable for a {age_level}.  Next add section called JUSTIFICATION explaining WHY this is being proposed."
    PROPOSITION = st.session_state.selected_prop

    with st.spinner(f'Generating {PAGE} summary...'):
      st.markdown(generatePrediction(PROPOSITION, USER_PROMPT))

      # TODO: add citations as links ...

# -------------------- Feedback --------------------
feedback_button = st.feedback("thumbs")
if feedback_button is not None:
  logUserFeedback(f"{PAGE}: feedback= {'+1' if feedback_button == 1 else '-1'}")
