# RAG-Agent

## Overview
This project implements a **Retrieval-Augmented Generation (RAG)** framework using the `phi` library. It combines specialized agents for web search and financial data retrieval, working together to deliver summarized insights.

## Features
- **Web Assistant**: Fetches concise, source-backed web updates.
- **Finance Assistant**: Retrieves financial data (e.g., stock prices, analyst recommendations).
- **Team Coordination**: Combines agents for multi-faceted tasks with structured outputs in Markdown and tables.

## Installation
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Create a `.env` file for api-key.

## Usage
Run the script to fetch financial insights and web summaries:
```bash
python main.py
```
