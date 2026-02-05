import typer
import sys
import os

# Create src module context if running from root
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from indexer import index_documents
from searcher import search_documents

app = typer.Typer(help="Local-Brain-Search: CLI for indexing and searching your personal docs.")

@app.command()
def index(path: str = typer.Argument(..., help="Path to the directory or file to index")):
    """
    Index a directory or file (Markdown, PDF, Text).
    """
    index_documents(path)

@app.command()
def search(query: str = typer.Argument(..., help="The search query text"), k: int = typer.Option(4, help="Number of results to return")):
    """
    Search your indexed documents.
    """
    search_documents(query, k)

if __name__ == "__main__":
    app()
