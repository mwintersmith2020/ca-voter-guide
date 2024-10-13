import functions
import streamlit as st
from langchain.llms import OpenAI
from PIL import Image

BOOK_IMAGE = Image.open("img/SOFTWAR-larry-ellison.jpeg")
PAGE = "🎓 Trivia"
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

Books are often full of anecdotes and quips that we forget over time.  Use this feature to rediscover those lost nuggets of wisdom.
""")

# -------------------- Slider --------------------
container = st.container(border=True)

genre = container.radio(
    "Show me a...",
    [
        "**:red[Larry Ellison]** quote  :speech_balloon:", 
        "***non-Larry Ellison*** quote", 
        "random fact about Ellison",
        "random fact about Oracle  :office:",
        "random fact about :rainbow[anything] :game_die:"
    ],
    index=0,
)

if genre:
  if 'quote' in genre:
    PROMPT = f'THIS IS A BOOK. BASED ON THE PROVIDED CONTEXT, select one random {genre}. Display it in the format "<quote>" --<author>.'
  else:
    PROMPT = f'THIS IS A BOOK. BASED ON THE PROVIDED CONTEXT, select and display one interesting or significant {genre} from the book.'
# if genre.startswith("**:red[Larry Ellison]**"):
# elif genre.startswith("***non-Larry Ellison***"):
# elif genre.startswith(""):
# elif genre.startswith(""):
# elif genre.startswith(""):
  
#   OPTION = genre
#   st.write(OPTION)


# -------------------- Output --------------------
with st.container(border=True):
  if st.button("Generate!"):
    #st.write(PROMPT)
    with st.spinner(f'Generating {PAGE} summary...'):
      docs = []

      # Get the answer from the chain
      res = functions.qa(PROMPT)
      answer, docs = res['result'], res['source_documents']

    #st.write(answer)
    modified_text = answer.strip().replace('\n',' ')

    if 'quote' in PROMPT:  # Clean up messy quotes ...
      quote_start = answer.find('"')  # Find the position of the first occurrence of "
      if quote_start > 1:  # Check if " is found
          modified_text = answer[quote_start:].replace("<quote>","").replace("</quote>","").replace("</ quote>","")
      else:
          modified_text = answer.replace("<quote>","").replace("</quote>","").replace("</ quote>","")
        
    st.markdown(f'***{modified_text}***')

