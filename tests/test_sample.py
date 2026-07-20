from pathlib import Path


def test_sample_file_exists():
    path = Path("data/sample_knowledge.txt")
    assert path.exists(), "El archivo de conocimiento no existe"
