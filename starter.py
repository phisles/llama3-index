"""
Run this script.
Make changes to update_app_function or any part of your script.
Stop the running interface (Ctrl+C in the terminal).
Run the script again to see the changes take effect.
"""

from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, Settings
from llama_index.core.embeddings import resolve_embed_model
from llama_index.llms.ollama import Ollama
import gradio as gr

documents = SimpleDirectoryReader("data").load_data()

# bge embedding model
Settings.embed_model = resolve_embed_model("local:BAAI/bge-small-en-v1.5")

# ollama
Settings.llm = Ollama(model="llama3", request_timeout=360.0)

index = VectorStoreIndex.from_documents(documents)
query_engine = index.as_query_engine()

def ask_question(query):
    prompt = ("You are a records analyst workign with a large set of documents, transcripts and other texts related to the user's investigation. "
              "assess the provided relevant document samples, and answer the question. You will tell the user which document the information is from. "
              "If the question cannot be answered based on the information provided, do not make anything up or make any assumptions. "
              "Here is the question: ")
    modified_query = prompt + query
    response = query_engine.query(modified_query)
    return response



interface = gr.Interface(fn=ask_question, inputs="text", outputs="text")
interface.launch()
