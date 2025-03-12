# 🦙 LlamaParse PDF Parsing Project

Welcome to the **LlamaParse PDF Parsing Project**! 🚀 This repository demonstrates how to use **LlamaParse**, an AI-powered document parsing tool, to extract structured data from PDFs efficiently. This project focuses on **loading, parsing, and extracting tables** from PDF documents using **Python** and **LlamaParse API**.

---

## 📌 Project Overview

### **Key Features**

✅ **Loads API Key Securely** using `dotenv` 🔑  
✅ **Parses PDF Documents** with **LlamaParse**  
✅ **Extracts Structured Data & Tables** from PDFs  
✅ **Handles Errors Gracefully** to avoid unexpected failures  

### **How It Works**

This script:

1. Loads API credentials from an **environment file (.env)**.
2. Initializes **LlamaParse** with the API key.
3. Parses a **PDF document** (`data/table.pdf`).
4. Extracts tables and prints them in a structured format.

---

## 🛠️ Setup & Installation

### **1️⃣ Prerequisites**

Make sure you have the following installed:

- Python 3.8+
- `pip` (Python package manager)
- `dotenv` for managing API keys
- `LlamaParse` library

### **2️⃣ Installation Steps**

Clone this repository and install dependencies:

```bash
# Clone the repository
git clone https://github.com/your-username/llama-parse-project.git
cd llama-parse-project

# Install required libraries
pip install -r requirements.txt
```

### **3️⃣ Setup API Key**

Create a `.env` file in the root directory and add your **Llama Cloud API Key**:

```bash
LLAMA_CLOUD_API_KEY=your_api_key_here
```

---

## 🚀 Usage

Run the script to **parse and extract tables** from a PDF:

```bash
python parse_pdf.py
```

If the API key is missing, the script will throw an error to remind you to set it up correctly.

---

## 📝 Code Breakdown

### **1️⃣ Load API Key**

```python
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("LLAMA_CLOUD_API_KEY")
```
Loads the API key from the `.env` file securely.

### **2️⃣ Initialize LlamaParse**

```python
from llama_parse import LlamaParse

parser = LlamaParse(api_key=api_key, result_type="markdown")
```
Creates an instance of **LlamaParse** with the provided API key.

### **3️⃣ Parse PDF Document**

```python
try:
    documents = parser.load_data("data/table.pdf")
    print(documents)
except Exception as e:
    print(f"Failed to parse the file: {e}")
```
Loads and parses the PDF document, handling errors gracefully.

### **4️⃣ Extract Tables**

```python
tables = []
if isinstance(documents, dict):
    tables = documents.get('tables', [])
elif isinstance(documents, list):
    for doc in documents:
        if isinstance(doc, dict):
            tables.append(doc.get('tables', []))

for table in tables:
    print(table)
```
Extracts **tables** from the parsed document and prints them.

---

## 🔥 Why Use LlamaParse?

✔️ **Fast & Efficient** PDF Parsing 📑  
✔️ **Extracts Structured Data** like Tables & Lists 📊  
✔️ **Easy API Integration** with Python 🐍  
✔️ **Handles Large Documents Seamlessly** 🚀  

---

## 📬 Contact & Contributions

💡 Want to improve this project? **Feel free to contribute!**  
📧 Reach out via **[Email](feenu.akhter@gmail.com)** or **[LinkedIn](https://www.linkedin.com/in/farheen-akhter-153a0b156/)**  

---

⭐ **If you find this project useful, don't forget to star ⭐ the repository!**

