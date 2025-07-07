# 🧪 PubMed Paper Fetcher CLI Tool

A command-line Python tool that fetches research papers from PubMed based on a given query, filters results to find papers with at least one **non-academic author affiliated with pharmaceutical or biotech companies**, and outputs the data to a **CSV file**.

---

## 🚀 Features

- 🔍 Full support for **PubMed's advanced query syntax**
- 🧬 Identifies authors affiliated with **non-academic companies**
- 📩 Extracts **corresponding author emails** (if available)
- 📦 CLI tool with options to:
  - Save results to a CSV
  - Print debug logs
- 🧪 Written in **typed Python** with unit tests
- 📁 Powered by **Poetry** for dependency and packaging
- ✅ Production-ready and open-source

---

## 📂 Output Format

The tool outputs a CSV with the following columns:

| Field                    | Description                                               |
|-------------------------|-----------------------------------------------------------|
| PubmedID                | Unique PubMed identifier                                  |
| Title                   | Title of the paper                                        |
| Publication Date        | Year or date of publication                               |
| Non-academic Author(s)  | Names of authors not affiliated with universities/labs    |
| Company Affiliation(s)  | Names of pharmaceutical or biotech companies              |
| Corresponding Author Email | Email of corresponding author (if available)           |

---

## 🛠️ Installation

> Requires Python **3.8+**

### 1. Clone the Repository

```bash
git clone https://github.com/gunjanrawat-gr/pubmed-paper-fetcher.git
cd pubmed-paper-fetcher
