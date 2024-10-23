import functions
import streamlit as st
from functions import logUserFeedback, generatePrediction
from layout_template import sidebar_template, render_radio


PAGE = "🤖 Election-GPT"

# -------------------- Sidebar Layout --------------------
sidebar_template()

# -------------------- Page Header --------------------
st.header(PAGE, divider=True)

st.markdown(f"""
### **Greetings, Voter {st.session_state.name}!**

##### Use this page to ask any free-form question you may have -- e.g. *What is the 5-year impact of this proposition*?
""")

# -------------------- Page Body --------------------
render_radio()

# -------------------- Chatbot --------------------
with st.container(border=True, height=500):
    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display chat messages from history on app rerun
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # React to user input
    if prompt := st.chat_input(f"What can I explain about {st.session_state.selected_prop.split('-')[0].strip()}?"):
        # Display user message in chat message container
        st.chat_message("user").markdown(prompt)
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})

        PROPOSITION = st.session_state.selected_prop

        with st.spinner(f'Generating {PAGE} response for *{PROPOSITION.split("-")[0].strip()}*...'):
            response= generatePrediction(PROPOSITION, prompt)

            # Display assistant response
            with st.chat_message("assistant"):
                st.markdown(response)

            # Add response to chat history
            st.session_state.messages.append({"role": "assistant", "content": response})

# -------------------- Feedback --------------------
feedback_button = st.feedback("thumbs")
if feedback_button is not None:
  logUserFeedback(f"{PAGE}: feedback= {'+1' if feedback_button == 1 else '-1'}")