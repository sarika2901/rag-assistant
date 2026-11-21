import importlib 
import sys
import urllib.request

print("Python:", sys.version.split()[0])

for pkg in ["numpy", "sentence_transformers", "openai", "dotenv"]:
    try:
        importlib.import_module(pkg)
        print("OK     ", pkg)
    except ImportError:
            print("MISSING", pkg)

try:
    urllib.request.urlopen("http://localhost:11434", timeout=3)
    print("OK     Ollama server reachable")
except Exception as e:
        print("PROBLEM Ollama not reachable", e)
