import os
from dotenv import load_dotenv
from llama_parse import LlamaParse

# Load API key from .env file
load_dotenv()
api_key = os.getenv("LLAMA_CLOUD_API_KEY")

if not api_key:
    raise ValueError("API key not found. Make sure LLAMA_CLOUD_API_KEY is set in your environment.")

# Initialize LlamaParse with api key
parser = LlamaParse(api_key=api_key, result_type="markdown")

# Parse the PDF document
try:
    documents = parser.load_data("data/table.pdf")
    print(documents)
except Exception as e:
    print(f"Failed to parse the file: {e}")

# Extract tables from the parsed content
tables = []
if isinstance(documents, dict):
    tables = documents.get('tables', [])
elif isinstance(documents, list):
    for doc in documents:
        if isinstance(doc, dict):
            tables.append(doc.get('tables', []))

for table in tables:
    print(table)
