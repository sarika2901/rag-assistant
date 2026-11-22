import re   #regex
from dataclasses import dataclass
from pathlib import Path

@dataclass
class Chunk:
    chunk_id: str      # unique ID, e.g. "leave_policy.txt::3"
    doc_name: str      # source file, needed for citations
    text: str          # the chunk content
    start_char: int    # where the chunk starts in the cleaned document
    end_char: int      # where it ends

def load_text_files(folder: str) -> dict[str, str]:
    """Read every .txt file in a folder. Returns {filename: raw_text}."""
    docs = {}
    for path in sorted(Path(folder).glob("*.txt")):
        docs[path.name] = path.read_text(encoding="utf-8", errors="ignore")
    return docs

def clean_text(text: str) -> str:
    """Normalize whitespace so chunk sizes are predictable."""
    text = text.replace("\r\n", "\n")        # Windows line endings -> standard
    text = re.sub(r"(?<=\S)[ \t]+", " ", text)   # collapse space runs, but NOT leading indentation
    text = re.sub(r"[ \t]+\n", "\n", text)       # remove trailing spaces at line ends
    #text = re.sub(r"[ \t]+", " ", text)      # collapse runs of spaces/tabs
    text = re.sub(r"\n{3,}", "\n\n", text)   # at most one blank line
    return text.strip()

def chunk_fixed(
    text: str,
    doc_name: str,
    chunk_size: int = 800,
    overlap: int = 150,
) -> list[Chunk]:
    """Split text into fixed-size character windows with overlap."""
    if overlap >= chunk_size:
        raise ValueError("overlap must be smaller than chunk_size")

    chunks = []
    step = chunk_size - overlap   # how far the window moves each time

    for i, start in enumerate(range(0, len(text), step)):
        end = min(start + chunk_size, len(text))
        piece = text[start:end].strip()
        if piece:
            chunks.append(
                Chunk(
                    chunk_id=f"{doc_name}::{i}",
                    doc_name=doc_name,
                    text=piece,
                    start_char=start,
                    end_char=end,
                )
            )
        if end == len(text):
            break

    return chunks