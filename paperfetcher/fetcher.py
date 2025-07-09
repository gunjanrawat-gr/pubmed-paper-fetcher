import requests
from typing import List, Dict
import xml.etree.ElementTree as ET

def fetch_pubmed_ids(query: str) -> List[str]:
    url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
    params = {
        "db": "pubmed",
        "term": query,
        "retmode": "json",
        "retmax": 10
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.json()['esearchresult']['idlist']

def fetch_pubmed_details(pubmed_ids: List[str]) -> List[Dict]:
    url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"
    params = {
        "db": "pubmed",
        "id": ','.join(pubmed_ids),
        "retmode": "xml"
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    root = ET.fromstring(response.text)

    results = []
    for article in root.findall(".//PubmedArticle"):
        pmid = article.findtext(".//PMID")
        title = article.findtext(".//ArticleTitle")
        date = article.findtext(".//PubDate/Year")
        authors = []
        for author in article.findall(".//Author"):
            name = f"{author.findtext('ForeName', '')} {author.findtext('LastName', '')}".strip()
            affiliation = author.findtext(".//AffiliationInfo/Affiliation", default="")
            email = ""
            if "@" in affiliation:
                email = affiliation.split()[-1]
            authors.append({
                "name": name,
                "affiliation": affiliation,
                "email": email
            })
        results.append({
            "pmid": pmid,
            "title": title,
            "date": date,
            "authors": authors
        })
    return results
