import functions
import streamlit as st
from langchain.llms import OpenAI
from PIL import Image

BOOK_IMAGE = Image.open("img/SOFTWAR-larry-ellison.jpeg")
PAGE = "📈 Strategy"
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

Explore the various facets of Oracle's business strategy.
""")

# -------------------- Slider --------------------
container = st.container(border=True)

genre = container.radio(
    "Perform a...",
    [
        "S.W.O.T. analysis of Oracle",
        "Analysis of how Oracle might outwit its strongest competitor",
        "Describe Oracle's strategy for competition and growth"
    ],
    index=0,
)

if genre:
  PROMPT = f'THIS IS A BOOK. BASED ON THE PROVIDED CONTEXT, generate a {genre} in markdown format, bolding each section heading.'
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
