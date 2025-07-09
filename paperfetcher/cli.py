import argparse
import csv
from paperfetcher.fetcher import fetch_pubmed_ids, fetch_pubmed_details
from paperfetcher.filters import extract_company_authors

def main():
    parser = argparse.ArgumentParser(description="Fetch PubMed papers with non-academic authors")

    # ✅ Use --query style optional arguments
    parser.add_argument('--query', type=str, required=True, help="Search term for PubMed")
    parser.add_argument('--max-results', type=int, default=10, help="Number of results to fetch")
    parser.add_argument('--output', type=str, default="results.csv", help="Output CSV file")
    parser.add_argument('--debug', action='store_true', help="Enable debug logs")

    args = parser.parse_args()

    # ✅ Just print for now to confirm it's working
    print(f"✅ CLI Working!")
    print(f"Query: {args.query}")
    print(f"Max results: {args.max_results}")
    print(f"Output file: {args.output}")
    if args.debug:
        print("Debug mode: ON")

if __name__ == "__main__":
    main()