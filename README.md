# 📊 Gemini-Powered SQL Data Retriever

An intuitive web application that allows users to interact with a SQL database using natural language. Built with **Streamlit**, **SQLite3**, and **Google Gemini 2.0 Flash**.



## 🌟 Overview

This project bridges the gap between non-technical users and relational databases. Instead of writing complex SQL queries, users can simply ask questions in plain English, and the app will:

1.  **Interpret** the question using Google Gemini.
2.  **Generate** the corresponding SQL query.
3.  **Execute** the query on a local `student.db` SQLite database.
4.  **Display** the results directly in the browser.

---

## 🛠️ Tech Stack

* **Language:** Python
* **LLM:** Google Gemini 2.0 Flash
* **Web Framework:** Streamlit
* **Database:** SQLite3
* **Environment Management:** `python-dotenv`

---

## 🚀 Getting Started

### 1. Prerequisites
* Python 3.10 or higher.
* A Google Cloud Project with the **Generative Language API** enabled to obtain an API Key.

### 2. Installation
Clone the repository and install the required dependencies:
```bash
git clone <your-repo-link>
cd <project-folder>
pip install -r requirements.txt
