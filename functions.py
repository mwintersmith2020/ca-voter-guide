#!/usr/bin/env python3
from langchain.chains import RetrievalQA
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain.vectorstores import Chroma
from langchain.llms import Ollama
import chromadb
from chromadb import Documents, EmbeddingFunction, Embeddings
from constants import CHROMA_SETTINGS

import os
import argparse
import time
import pdb

print("Initializing variables ...")
model = os.environ.get("MODEL", "llama3")
embeddings_model_name = os.environ.get("EMBEDDINGS_MODEL_NAME", "hkunlp/instructor-large")
os.environ['HF_HUB_OFFLINE'] = '1'

persist_directory = os.environ.get("PERSIST_DIRECTORY", "db")
target_source_chunks = int(os.environ.get('TARGET_SOURCE_CHUNKS',4))

print("Loading embeddings...")
embeddings = HuggingFaceEmbeddings(model_name=embeddings_model_name)

print("Loading vector db...")
db = Chroma(persist_directory=persist_directory, embedding_function=embeddings)

print("Initializing retriever...")
retriever = db.as_retriever(search_kwargs={"k": target_source_chunks})

print("Initializing LLM...")
callbacks = [] #if args.mute_stream else [StreamingStdOutCallbackHandler()]
llm = Ollama(model=model, callbacks=callbacks, temperature=0.5)
qa = RetrievalQA.from_chain_type(llm=llm, chain_type="stuff", retriever=retriever, return_source_documents= True) #not args.hide_source)
    
print("Done.")
