import sys
sys.path.insert(0, "src")

from chunking import clean_text, chunk_fixed

text = clean_text("Hello world. " * 200)
print("Text length:", len(text))

chunks = chunk_fixed(text, "demo.txt", chunk_size=300, overlap=50)
print(len(chunks), "chunks")
print("Chunk 0 ends with:  ", repr(chunks[0].text[-50:]))
print("Chunk 1 starts with:", repr(chunks[1].text[:50]))
print("Same?", chunks[0].text[-50:] == chunks[1].text[:50])