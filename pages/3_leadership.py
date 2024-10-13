import functions
import streamlit as st
from langchain.llms import OpenAI
from PIL import Image

BOOK_IMAGE = Image.open("img/SOFTWAR-larry-ellison.jpeg")
PAGE = "👑 Leadership"
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

Larry Ellison had a unique leadership style -- explore it further below.
""")

# -------------------- Slider --------------------
container = st.container(border=True)

genre = container.radio(
    "Perform a...",
    [
        "List Ellison's *strengths* and *weaknesses* as a business leader",
        "List 3 pivotal moments in Ellison's tenure at Oracle"
    ],
    index=0,
)

if 'strengths' in genre:
  PROMPT = f'THIS IS A BOOK. BASED ON THE PROVIDED CONTEXT, generate a {genre} and output as a markdown table, with Strengths in one column and weaknesses in another'
else:
  PROMPT = f'THIS IS A BOOK. BASED ON THE PROVIDED CONTEXT, {genre} as an unordered list.'
  # if 'quote' in genre:
  #   PROMPT = f'THIS IS A BOOK. BASED ON THE PROVIDED CONTEXT, generate a {genre} in markdown format, bolding each section heading.'
  # else:
  #   PROMPT = f'THIS IS A BOOK. BASED ON THE PROVIDED CONTEXT, select and display one interesting or significant {genre} from the book.'

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
