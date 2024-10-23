import functions
import streamlit as st
from layout_template import sidebar_template


PAGE = "🗳️ Summary of Propositions"
PROMPT = ''

answer, docs = '', []
# -------------------- Sidebar Layout --------------------
sidebar_template()

# -------------------- Page Header --------------------
st.header(PAGE, divider=True)

st.markdown("""
### **Greetings, Voter!**

Generative A.I. can help demystify the voting process by providing interative tools which allow you to ask questions in plain English.
""")

# -------------------- Page Body --------------------
container = st.container(border=True)

genre = container.radio(
    "Tell me more about ...",
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
        "Proposition 36 - **Allows Felony Charges and Increases Sentences for Drug and Theft Crimes.**",
    ],
    index=0,
)

if genre:
  if 'quote' in genre:
    PROMPT = f'THIS IS A BOOK. BASED ON THE PROVIDED CONTEXT, select one random {genre}. Display it in the format "<quote>" --<author>.'
  else:
    PROMPT = f'THIS IS A BOOK. BASED ON THE PROVIDED CONTEXT, select and display one interesting or significant {genre} from the book.'

# -------------------- Output --------------------
with st.container(border=True):
  if st.button("Ask!"):
    st.write(PROMPT)
#     with st.spinner(f'Generating {PAGE} summary...'):
#       docs = []

#       # Get the answer from the chain
#       res = functions.qa(PROMPT)
#       answer, docs = res['result'], res['source_documents']

#     #st.write(answer)
#     modified_text = answer.strip().replace('\n',' ')

#     if 'quote' in PROMPT:  # Clean up messy quotes ...
#       quote_start = answer.find('"')  # Find the position of the first occurrence of "
#       if quote_start > 1:  # Check if " is found
#           modified_text = answer[quote_start:].replace("<quote>","").replace("</quote>","").replace("</ quote>","")
#       else:
#           modified_text = answer.replace("<quote>","").replace("</quote>","").replace("</ quote>","")
        
#     st.markdown(f'***{modified_text}***')

