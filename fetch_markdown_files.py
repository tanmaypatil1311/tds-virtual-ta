import os
import requests

# All markdown URLs based on your sidebar structure
md_pages = [
    # Development Tools
    "development-tools",
    "github-copilot",
    "github-codespaces",
    "gitpod",
    "docker",
    "github-actions",
    "webapp-basics",
    
    # Deployment Tools
    "gradio",
    "streamlit",
    "langchain-deploy",
    
    # Large Language Models
    "prompt-engineering",
    "generative-ai",
    "openai-api",
    "langchain",
    "langgraph",
    "retrieval",
    "function-calling",
    "semantic-kernel",
    
    # Data Sourcing
    "data-sourcing",
    "data-stores",
    "llamaindex",
    "web-scraping",
    "pdf",
    
    # Data Preparation
    "data-cleaning",
    "text-cleaning",
    "translation",
    "ocr",
    
    # Data Analysis
    "data-analysis",
    "time-series",
    "sentiment-analysis",
    "eda",
    
    # Data Visualization
    "data-visualization",
    "dashboards",
]

# Base URL
base_url = "https://tds.s-anand.net"

# Output directory
output_dir = "tds_markdown"
os.makedirs(output_dir, exist_ok=True)

# Download each markdown file
for page in md_pages:
    url = f"{base_url}/{page}.md"
    output_path = os.path.join(output_dir, f"{page}.md")
    
    print(f"Fetching {url} ...")
    try:
        response = requests.get(url)
        response.raise_for_status()
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(response.text)
        print(f"✅ Saved to {output_path}")
    except requests.HTTPError as e:
        print(f"❌ Failed to fetch {url}: {e}")

print("\n✅ All markdown files downloaded.")
