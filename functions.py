import sys
import os
import json
import argparse
import logging
import time
import pdb
import requests
import streamlit as st
import chromadb
import replicate

from chromadb.config import Settings
from chromadb import Documents

USER_IP = '<unknown>'
USER_NAME = "Joe"
st.session_state.name = ''

# Define the embedding function
class ReplicateEmbeddingFunction:
    def __call__(self, input: Documents):
        embedding_dict = replicate.run(
            embeddings_model_name,
            input={"text": json.dumps(input)}
        )
        return [item["embedding"] for item in embedding_dict]
    
def logUserFeedback(message):
    logging.info(f"{USER_IP}: {message}")

def getContext(criterion_text):
    results = collection.query(
        query_texts=criterion_text,
        n_results=target_source_chunks,
    )
    citations = '\n'.join(results['documents'][0])
    return citations

def getPrediction(prompt_template):
    model_response = replicate.run(
        model,
        input={"prompt": prompt_template}
    )

    # Concatenate the response into a single string.
    response = ''.join([str(s) for s in model_response])
    return response

def generatePrediction(PROPOSITION, USER_PROMPT):
    logUserFeedback(f"PROPOSITION= {PROPOSITION}")
    logUserFeedback(f"USER_PROMPT= {USER_PROMPT}")

    CITATIONS = getContext(PROPOSITION)
    PROMPT_TEMPLATE = f"""
This is an informational packet about: {PROPOSITION.upper()}.  You will be given a USER_PROMPT and a list of CITATIONS.

Make sure that your responses is strictly limited to CITATIONS.  Do not include information not found in CITATIONS.

USER_PROMPT: {USER_PROMPT}

CITATIONS: {CITATIONS}
"""
    text = getPrediction(PROMPT_TEMPLATE)

    # Now do some post-processing ...
    # ... to use a markdown-compatible bullet symbol ...
    # ... to prevent '$' from trigger latex math-symbol mode ...
    modified_text = text.replace('• ','* ').replace('$','\$')
    return modified_text

# -------------------- Start initialization --------------------

st.set_page_config(layout="wide")

model = os.environ.get("MODEL_NAME", "llama3")
embeddings_model_name = os.environ.get("EMBEDDINGS_MODEL_NAME", "hkunlp/instructor-large")

# -------------------- Initialize logging --------------------

logging.basicConfig(level=logging.INFO)
logging.info("------------ New Session ------------")
logging.info("Initializing variables ...")
ip_request = requests.get('https://api.ipify.org?format=json')
USER_IP = ip_request.json()['ip']
logging.info(f"USER_IP= {USER_IP}")

# -------------------- Initialize models --------------------

model = os.environ.get("MODEL_NAME", "llama3")
embeddings_model_name = os.environ.get("EMBEDDINGS_MODEL_NAME", "hkunlp/instructor-large")
persist_directory = os.environ.get("PERSIST_DIRECTORY", "db")
target_source_chunks = int(os.environ.get('TARGET_SOURCE_CHUNKS',5))

logging.info("Initializing chroma db...")
client = chromadb.PersistentClient(path=persist_directory)

logging.info("Initializing embedding function...")
embedding_function = ReplicateEmbeddingFunction()

logging.info("Loading collection...")
collection = client.get_collection(name="voter-guide", embedding_function=embedding_function)

logging.info("Done.")
