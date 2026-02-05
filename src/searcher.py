from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from rich.console import Console
from rich.panel import Panel
from rich.markdown import Markdown

console = Console()
DB_DIR = "./local_brain_db"

def search_documents(query: str, k: int = 4):
    console.print(f"[bold blue]Searching for:[/bold blue] '{query}'")
    
    embedding_function = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    
    # Load from disk
    try:
        vectorstore = Chroma(
            persist_directory=DB_DIR, 
            embedding_function=embedding_function
        )
    except Exception as e:
        console.print("[red]Error loading database. Did you run 'index' first?[/red]")
        return

    results = vectorstore.similarity_search_with_score(query, k=k)
    
    if not results:
        console.print("[yellow]No relevant results found.[/yellow]")
        return

    for doc, score in results:
        source = doc.metadata.get("source", "Unknown")
        abs_source = os.path.abspath(source)
        content = doc.page_content
        
        # Determine relevance - L2 distance for Chroma: lower is better. 
        # Typically 0.0 to 2.0 range for many models.
        panel_header = f"[bold]Source:[/bold] {abs_source}\n[bold]Relevance Score:[/bold] {score:.4f}"
        console.print(Panel(content, title=panel_header, border_style="cyan", padding=(1, 2)))
