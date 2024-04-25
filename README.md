# Llama3 Index Application

## Overview
The Llama3 Index Application leverages advanced natural language processing technologies to provide an intuitive query interface for analyzing large sets of documents. It incorporates the Llama3 model provided by Ollama, utilizing a vector store index for efficient information retrieval.

## Key Features
- **Document Processing**: Automatically loads and indexes documents from a specified directory.
- **Advanced Embedding Model**: Uses the `local:BAAI/bge-small-en-v1.5` embedding model from Hugging Face to ensure rich, contextual embedding of text.
- **Intelligent Query Interface**: Employs Gradio to provide a user-friendly web interface, allowing users to input queries and receive responses seamlessly.
- **Context-Aware Responses**: Enhances queries with a predefined context that the system functions as a records analyst, ensuring that responses are accurate and document-based.

## Usage
1. **Start the Application**: Run the script to launch the Gradio interface.
2. **Input Queries**: Type your questions into the Gradio interface to analyze the indexed documents.
3. **Receive Responses**: The application assesses the relevant document samples and returns the most pertinent information, including the source document for transparency.

## Development
- **Modify and Extend**: Make changes to the application functions as needed. Restart the application to see changes take effect:
  - local server where the app runs: http://127.0.0.1:7860/
  - Stop the running interface using `Ctrl+C`.
  - Re-run the script to launch the updated interface.

## Technologies Used
- **Gradio**: Offers an easy-to-use interface for interacting with the machine learning model.
- **Hugging Face Embeddings**: Provides state-of-the-art embedding models for text analysis.
- **Vector Store Index**: Facilitates quick retrieval of information from a large dataset of documents.

## Installation and Setup
Ensure you have Python and necessary packages installed:
```bash
pip install gradio huggingface_hub
