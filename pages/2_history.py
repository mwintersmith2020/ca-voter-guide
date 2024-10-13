import functions
import streamlit as st
from langchain.llms import OpenAI
from PIL import Image

PROMPT = "provide a list of the 25 most influential people in Oracle's success, in sorted order"
BOOK_IMAGE = Image.open("img/SOFTWAR-larry-ellison.jpeg")
PAGE = "🏛️ History"
PROMPT = ''

answer, docs = '', []
# -------------------- Sidebar Layout --------------------
with st.sidebar:
	st.image(BOOK_IMAGE)
	st.sidebar.markdown("---")

# -------------------- Page Header --------------------
st.header(PAGE, divider=True)

st.markdown("""
### **Greetings, Book Lover!**

Use this page to explore the nuances of Oracle's history.
""")

# -------------------- Slider --------------------
container = st.container(border=True)

genre = container.radio(
    "Choose an option below:",
    [
        "The History of Oracle",
        "List, year-by-year all the significant events in Oracle's history (e.g. 1977 - Oracle founded..., 1978 - ...)",
        "List of the top 3 to 5 deals which propelled Oracle to an industry lead"
    ],
    index=0,
)

if genre:
  PROMPT = f'THIS IS A BOOK. BASED ON THE PROVIDED CONTEXT, generate {genre} as a markdown unordered list.'

# -------------------- Output --------------------
with st.container(border=True):
  if st.button("Generate!"):
    #st.write(PROMPT)
    with st.spinner(f'Generating {PAGE} summary...'):
      docs = []

      # Get the answer from the chain
      res = functions.qa(PROMPT)
      answer, docs = res['result'], res['source_documents']

    st.markdown(answer)

    st.markdown("____ SOURCES ____")
    # Sort the docs list by the "source" metadata field
    for document in sorted(docs, key=lambda document: document.metadata["source"]):
      st.button(document.metadata["source"], help=document.page_content, type="secondary")