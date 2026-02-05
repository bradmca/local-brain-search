import os
from typing import List
from pathlib import Path
from langchain_community.document_loaders import TextLoader, PyPDFLoader
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from langchain_text_splitters import RecursiveCharacterTextSplitter
from rich.console import Console

console = Console()

DB_DIR = "./local_brain_db"

def load_documents(path: str) -> List:
    documents = []
    path_obj = Path(path)
    
    if not path_obj.exists():
        console.print(f"[red]Error: Path {path} does not exist.[/red]")
        return []

    files_to_process = []
    if path_obj.is_file():
        files_to_process.append(path_obj)
    else:
        # Recursive search for supported formats
        extensions = ['*.md', '*.txt', '*.pdf']
        for ext in extensions:
            files_to_process.extend(path_obj.rglob(ext))

    with console.status(f"[bold green]Loading {len(files_to_process)} files..."):
        for file_path in files_to_process:
            try:
                if file_path.suffix.lower() == '.pdf':
                    loader = PyPDFLoader(str(file_path))
                    documents.extend(loader.load())
                elif file_path.suffix.lower() == '.txt':
                    loader = TextLoader(str(file_path), encoding='utf-8')
                    documents.extend(loader.load())
                elif file_path.suffix.lower() == '.md':
                    # Using TextLoader for markdown often works better for simple raw text indexing 
                    # than Unstructured depending on dependencies, but let's try TextLoader first for speed.
                    loader = TextLoader(str(file_path), encoding='utf-8')
                    documents.extend(loader.load())
            except Exception as e:
                console.print(f"[yellow]Skipping {file_path}: {e}[/yellow]")
                
    return documents

def index_documents(source_path: str):
    console.print(f"[bold blue]Scanning {source_path}...[/bold blue]")
    docs = load_documents(source_path)
    
    if not docs:
        console.print("[yellow]No documents found to index.[/yellow]")
        return

    console.print(f"[green]Found {len(docs)} documents. Splitting text...[/green]")
    
    # Split text
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len,
    )
    splits = text_splitter.split_documents(docs)
    console.print(f"[green]Created {len(splits)} chunks.[/green]")

    # Embed and Store
    console.print("[bold blue]Embedding and storing in local ChromaDB...[/bold blue]")
    embedding_function = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    
    # Initialize Chroma with persistence
    # Note: Chroma will automatically persist by default in newer versions if persistent_path is given
    vectorstore = Chroma.from_documents(
        documents=splits,
        embedding=embedding_function,
        persist_directory=DB_DIR
    )
    
    console.print(f"[bold green]Success! Indexed {len(splits)} chunks to {DB_DIR}[/bold green]")
