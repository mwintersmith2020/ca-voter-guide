import time
import functions
import streamlit as st
from langchain.llms import OpenAI
from PIL import Image

from layout_template import sidebar_template

#BOOK_IMAGE = Image.open("img/SOFTWAR-larry-ellison.jpeg")
PAGE = "📖 Overview"
answer, docs = '', []

#st.logo(image=BOOK_IMAGE, icon_image=None)

#st.sidebar.image(BOOK_IMAGE)

sidebar_template()
## -------------------- Functions --------------------
# def generate_response():
#   with st.spinner('Generating summary...'):
#     st.write(PROMPT)

#     # Get the answer from the chain
#     res = functions.qa(PROMPT)
#     answer, docs = res['result'], res['source_documents']

#   st.info(answer)
#   st.markdown("____ SOURCES ____")
#   for document in docs:
#     st.button(document.metadata["source"], help='Click to display source text.')

# -------------------- Sidebar Layout --------------------
# with st.sidebar:
# 	#st.image(BOOK_IMAGE)
#   st.sidebar.markdown("---")

#   st.sidebar.page_link("pages/user-agent.py", label="User Agent")
#   # Trust-o-Meter
#   #st.sidebar.page_link("app.py", label="Trust-o-Meter")
#   # Summary
#   # Winners & Losers
#   # Trojan Horses...
#   # Show Me The Money!
#   # Election-GPT


# -------------------- Page Header --------------------
st.header(PAGE, divider=True)

st.markdown("""
### **Greetings, Book Lover!**

This page allows you to create summaries where you can dynamically zoom in and out on granularity.

Zoom out to creat an **Amazon** style capsule summary or zoom in to create a **Blinkist** style summary.

Use the slider below to adjust this.
""")

# -------------------- Slider --------------------
container = st.container(border=True)

summary_length = container.slider("Choose summary length:", 1, 25, 5)
#PROMPT = f'BASED ON THE PROVIDED CONTEXT ONLY, summarize the text in {summary_length} lines.'
PROMPT = f'THIS IS A BOOK.  BASED ON THE PROVIDED CONTEXT, provide a {summary_length} bullet summary of the book.'
st.write("Generate a ", summary_length, "line summary.")

# -------------------- Output --------------------
with st.container(border=True):
  if st.button("Generate!"):
    with st.spinner(f'Generating {PAGE}...'):
      #st.write(PROMPT)
      docs = []

      # Get the answer from the chain
      res = functions.qa(PROMPT)
      answer, docs = res['result'], res['source_documents']

    st.info(answer)

    st.markdown("____ SOURCES ____")
    # Sort the docs list by the "source" metadata field
    for document in sorted(docs, key=lambda document: document.metadata["source"]):
      st.button(document.metadata["source"], help=document.page_content, type="secondary")



