#  Insurance Claim Bot: Web Scraper + Embedding Pipeline

This project scrapes data from the web, processes it using BeautifulSoup, and generates semantic embeddings using HuggingFace models through `llama-index`. The goal is to prepare text data for use in vector search or LLM-based QA systems.

---

##  Features

- Web scraping using `Playwright` (async headless browser)
- HTML parsing with `BeautifulSoup`
- Text embedding using `llama-index` and `HuggingFaceEmbedding`
- Progress visualization with `tqdm`
-  Clean modular Python code
--
##  Installation

###  Clone the repository
```bash
git clone https://github.com/your-username/insurance-claim-bot.git
cd insurance-claim-bot
```

###  Create environment (recommended)
```bash
conda create -n insurance_claim_bot python=3.10
conda activate insurance_claim_bot
```

### Install dependencies
```bash
pip install -r requirements.txt
```

**OR manually:**
```bash
pip install llama-index==0.10.30
pip install sentence-transformers
pip install beautifulsoup4 requests tqdm
pip install playwright
playwright install
pip install pyarrow==14.0.2
```

---

##  Usage

```python
# main.py or notebook

from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from playwright.async_api import async_playwright
from bs4 import BeautifulSoup
import requests

# Your scraping & embedding logic here
```

Make sure to run `playwright install` after installing the package.

---

##  Example Output

The script extracts text from webpages and transforms it into embeddings that can be used in:

- Vector search (e.g., Chroma, FAISS, Weaviate)
- LLM-based QA applications
- Document classification

---

##  Directory Structure

```
insurance-claim-bot/
│
├── main.py
├── utils.py
├── README.md
├── requirements.txt
└── data/
    └── scraped_pages/
```

---

##  Known Issues

- Ensure `pyarrow==14.0.2` is used to avoid `ArrayStatistics` or `parquet` import errors.
- Kernel restart may be needed after upgrading dependencies.

---

##  References

- [LlamaIndex Documentation](https://docs.llamaindex.ai/)
- [HuggingFace Sentence Transformers](https://www.sbert.net/)
- [Playwright Python Docs](https://playwright.dev/python/)

---

##  Author

Divyanshu Singh • AI/ML Developer  
[LinkedIn](https://www.linkedin.com/in/your-profile) | [GitHub](https://github.com/your-username)
