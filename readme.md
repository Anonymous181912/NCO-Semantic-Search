# NCO Semantic Search with Cross-Encoder Re-ranking
## Overview
This project implements a dual-stage semantic search system for the **National Classification of Occupations (NCO)** dataset. The goal is to allow users to search for relevant NCO job roles using natural language queries.

## Problem Statement
The NCO dataset contains thousands of job roles categorized by codes and sectors. Currently, access is limited to exact keyword lookups and static PDF files, which makes it hard to retrieve relevant information using flexible or natural queries.

## Approach
We use a **two-stage retrieval pipeline**:
1. **Vector Search (Dense Retrieval):** We use a bi-encoder model (`BAAI/bge-m3`) to embed all NCO titles/descriptions. FAISS is used to retrieve the top 50 most similar entries based on query embedding.
2. **Cross-Encoder Re-ranking:** A cross-encoder (`cross-encoder/ms-marco-MiniLM-L-6-v2`) re-evaluates the top 50 results. It scores them by contextual relevance and sorts them accordingly.

## Output
Given a user query, the system returns the most relevant NCO entries along with:
- NCO Title
- NCO Code
- Relevance Score

## Tools & Models
- **Bi-Encoder:** `BAAI/bge-m3`
- **Cross-Encoder:** `cross-encoder/ms-marco-MiniLM-L-6-v2`
- **Vector Search:** FAISS
- **PDF Parsing (optional):** `pdfplumber`

## Status
- NCO entries parsed and embedded
- Vector index created using FAISS
- Re-ranking implemented with cross-encoder

## Usage
- Accepts a natural language query as input
- Returns top NCO entries ranked by semantic relevance
