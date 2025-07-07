import argparse
import csv
from get_papers.fetcher import fetch_pubmed_ids, fetch_pubmed_details
from get_papers.filters import extract_company_authors

def main():
    parser = argparse.ArgumentParser(description="Fetch PubMed papers with pharma/biotech authors.")
    parser.add_argument("query", help="PubMed query")
    parser.add_argument("-d", "--debug", action="store_true", help="Show debug info")
    parser.add_argument("-f", "--file", help="Filename to save as CSV")

    args = parser.parse_args()
    pubmed_ids = fetch_pubmed_ids(args.query)

    if args.debug:
        print("Fetched PubMed IDs:", pubmed_ids)

    papers = fetch_pubmed_details(pubmed_ids)
    results = []

    for paper in papers:
        non_academic_authors, companies, email = extract_company_authors(paper["authors"])
        if non_academic_authors:
            results.append({
                "PubmedID": paper["pmid"],
                "Title": paper["title"],
                "Publication Date": paper["date"],
                "Non-academic Author(s)": "; ".join(non_academic_authors),
                "Company Affiliation(s)": "; ".join(companies),
                "Corresponding Author Email": email
            })

    if args.file:
        with open(args.file, "w", newline='') as f:
            writer = csv.DictWriter(f, fieldnames=results[0].keys())
            writer.writeheader()
            writer.writerows(results)
        print(f"Saved to {args.file}")
    else:
        for row in results:
            print(row)

if __name__ == "__main__":
    main()
