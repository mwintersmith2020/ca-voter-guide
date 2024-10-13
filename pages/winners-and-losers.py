import pdb
import functions
import streamlit as st
from langchain.llms import OpenAI

from layout_template import sidebar_template

PAGE = "🎲 Winners & Losers"
PROMPT = ''

answer, docs = '', []

# Set page to wide mode
st.set_page_config(layout="wide")

# -------------------- Sidebar Layout --------------------
sidebar_template()

# -------------------- Page Header --------------------
st.header(PAGE, divider=True)

st.markdown("""
Every proposed new legislation has winners and losers.  This page uses generative AI to determine (as best it can) who the winners and losers are for the propositions on the November ballot.
""")
# -------------------- Slider --------------------
container = st.container(border=True)

prop = container.radio(
    "Choose one:",
    [
        "Proposition 2 - **Authorizes Bonds for Public School and Community College Facilities.**",
        "Proposition 3 - **Constitutional Right to Marriage.**",
        "Proposition 4 - **Authorizes Bonds for Safe Drinking Water, Wildfire Prevention, and Climate Risks.**",
        "Proposition 5 - **Allows Local Bonds for Affordable Housing and Public Infrastructure.**",
        "Proposition 6 - **Eliminates Constitutional Provision Allowing Involuntary Servitude for Incarcerated Persons.**",
        "Proposition 32 - **Raises Minimum Wage.**",
        "Proposition 33 - **Expands Local Governments' Authority to Enact Rent Control on Residential Property.**",
        "Proposition 34 - **Restricts Spending of Prescription Drug Revenues by Health Care Providers.**",
        "Proposition 35 - **Provides Permanent Funding for Medi-Cal Health Care Services.**",
        "Proposition 36 - **Allows Felony Charges and Increases Sentences for Drug and Theft Crimes.**"
    ],
    index=0,
)

if prop:
    prop_num = prop.split('-')[0].strip()
    PROMPT = f'THIS IS AN INFORMATIONAL PUBLICATION. BASED ON THE PROVIDED CONTEXT, Write a list of WINNERS and LOSERS for {prop_num}; Create a WINNERS section with a bulleted list of who wins create a LOSERS sections with a bulleted list of who loses?'

# -------------------- Output --------------------
with st.container(border=True):
  if st.button("Generate!"):
    #st.write(PROMPT)
    with st.spinner(f'Generating {PAGE} summary for {prop_num}...'):
      docs = []

      # Get the answer from the chain
      res = functions.qa(PROMPT)
      answer, docs = res['result'], res['source_documents']

    formatted_answer = answer.replace('.\n•','.  \n•')
    st.markdown(formatted_answer)
    #pdb.set_trace()
    feedback = st.feedback("thumbs")
# -------------------- Feedback --------------------
