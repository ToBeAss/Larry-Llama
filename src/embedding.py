import os
import shutil
from langchain.schema.document import Document
from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma

CHROMA_PATH = "chroma"
DATA_PATH = "data"

def get_embedding():
    return OllamaEmbeddings(model = "nomic-embed-text")

def get_db():
    return Chroma(persist_directory = CHROMA_PATH, embedding_function = get_embedding())

# STEP 1: LOAD DATA FROM DOCUMENTS
def load_documents(path: str):
    document_loader = PyPDFDirectoryLoader(path)
    return document_loader.load()

# STEP 2: SPLIT DATA INTO SMALLER CHUNKS
def split_documents(documents: list[Document]):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size = 800,
        chunk_overlap = 400,
        length_function = len,
        is_separator_regex = False,
    )
    return text_splitter.split_documents(documents)

# STEP 3: EMBED DATA CHUNKS TO VECTOR STORE
def add_chunks_to_db(chunks: list[Document]):
    db = get_db()

    indexed_chunks = calculate_chunk_indexes(chunks)

    # Add or Update index library
    existing_items = db.get(include = []) # IDs are always included by default
    existing_ids = set(existing_items["ids"])
    print(f"Number of existing documents in DB: {len(existing_ids)}")

    # Only add documents that don't exist in the DB.
    new_chunks = []
    for chunk in indexed_chunks:
        if chunk.metadata["id"] not in existing_ids:
            new_chunks.append(chunk)

    if len(new_chunks):
        print(f"👉 Adding new documents: {len(new_chunks)}")
        new_chunk_ids = [chunk.metadata["id"] for chunk in new_chunks]
        db.add_documents(new_chunks, ids = new_chunk_ids)
        #db.persist()
    else:
        print("✅ No new documents to add")

def calculate_chunk_indexes(chunks):

    # This will create IDs like "data/produktspesifikasjon.pdf:6:2"
    # Page Source : Page Number : Chunk Index

    last_page_id = None
    current_chunk_index = 0

    for chunk in chunks:
        source = chunk.metadata.get("source")
        page = chunk.metadata.get("page")
        current_page_id = f"{source}:{page}"

        # If the page ID is the same as the last one, increment the index.
        if current_page_id == last_page_id:
            current_chunk_index += 1
        else:
            current_chunk_index = 0

        # Calculate the chunk ID.
        chunk_id = f"{current_page_id}:{current_chunk_index}"
        last_page_id = current_page_id

        # Add it to the page meta-data.
        chunk.metadata["id"] = chunk_id

    return chunks

def clear_database():
    if os.path.exists(CHROMA_PATH):
        shutil.rmtree(CHROMA_PATH)
    print("The database has been cleared")


# STEP 4: RETRIEVE RELEVANT DATA FROM DATABASE
def query_db(query: str):
    db = get_db()

    # Søker i databasen.
    # Finner de 5 mest relevante dokumentene basert på likhet med query, velger ut den ene mest relevante, ved hjelp av Maximal Marginal Relevance (MMR) 
    retriever = db.as_retriever(
        search_type="mmr", search_kwargs={"k": 5, "fetch_k": 20}
    )
    results = retriever.invoke(query)
    return results


documents = load_documents(DATA_PATH)
chunks = split_documents(documents)
add_chunks_to_db(chunks)