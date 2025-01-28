import argparse
from get_papers_list.api import PubMedAPI
from get_papers_list.filters import extract_non_academic_authors
from get_papers_list.csv_writer import save_to_csv
import os
from dotenv import load_dotenv

def main():
    load_dotenv()  # Load environment variables from .env file
    parser = argparse.ArgumentParser(description="Fetch research papers from PubMed.")
    parser.add_argument("query", help="Search query")
    parser.add_argument("-d", "--debug", action="store_true", help="Enable debug output")
    parser.add_argument("-f", "--file", help="Specify output filename")
    args = parser.parse_args()

    # Initialize the PubMed API with the API key from .env
    api = PubMedAPI(os.getenv("PUBMED_API_KEY"))
    
    # Fetch paper IDs using esearch
    paper_ids = api.fetch_papers(args.query)
    
    if not paper_ids:
        print("No papers found for the given query.")
        return
    
    # Fetch detailed data for those paper IDs
    papers = api.fetch_paper_details(paper_ids)

    if args.debug:
        print("Debug: Fetched papers structure:", papers)  # Print the structure of fetched papers

    if not papers:
        print("No detailed papers found.")
        return

    # Process and filter papers
    filtered_papers = extract_non_academic_authors(papers)

    if args.debug:
        print("Debug: Filtered papers:", filtered_papers)

    # If a filename is specified, save to CSV; otherwise, print results
    if args.file:
        save_to_csv(filtered_papers, args.file)
        print(f"Results saved to {args.file}")
    else:
        for paper in filtered_papers:
            print(paper)
