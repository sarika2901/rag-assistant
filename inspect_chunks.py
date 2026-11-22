import sys
sys.path.insert(0, "src")

from chunking import load_text_files, clean_text, chunk_fixed

CHUNK_SIZE = 800
OVERLAP = 150

docs = load_text_files("data/docs")
print(f"Loaded {len(docs)} documents\n")

all_chunks = []
for name, raw in docs.items():
    cleaned = clean_text(raw)
    chunks = chunk_fixed(cleaned, name, CHUNK_SIZE, OVERLAP)
    print(f"{name:40s} raw={len(raw):6d}  cleaned={len(cleaned):6d}  chunks={len(chunks)}")
    all_chunks.extend(chunks)

lengths = [len(c.text) for c in all_chunks]
print(f"\nTotal chunks: {len(all_chunks)}")
print(f"Chunk length  min={min(lengths)}  avg={sum(lengths)//len(lengths)}  max={max(lengths)}")

# Show a few chunks with visible boundaries
print("\n" + "=" * 70)
for chunk in all_chunks[:3]:
    print(f"[{chunk.chunk_id}]  chars {chunk.start_char}-{chunk.end_char}")
    print(">>>" + chunk.text + "<<<")
    print("-" * 70)