import pytest
import os
from indexer import load_documents
from searcher import search_documents

def test_load_documents_invalid_path():
    # Test that an invalid path returns an empty list
    docs = load_documents("./non_existent_folder")
    assert docs == []

def test_file_structure():
    # Verify core files exist
    assert os.path.exists("src/main.py")
    assert os.path.exists("src/indexer.py")
    assert os.path.exists("src/searcher.py")
    assert os.path.exists("requirements.txt")
