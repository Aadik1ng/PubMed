import requests
from typing import List
import os
from dotenv import load_dotenv

class PubMedAPI:
    BASE_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils"

    def __init__(self, api_key: str = None):
        load_dotenv()
        self.api_key = api_key or os.getenv("PUBMED_API_KEY")

    def fetch_papers(self, query: str) -> List[str]:
        params = {
            "db": "pubmed",
            "term": query,
            "retmode": "json",
            "retmax": 100,
            "api_key": self.api_key,
        }
        response = requests.get(f"{self.BASE_URL}/esearch.fcgi", params=params)
        response.raise_for_status()
        return response.json().get("esearchresult", {}).get("idlist", [])

    def fetch_paper_details(self, pmids: List[str]) -> str:
        if not pmids:
            raise ValueError("PMID list is empty. Cannot fetch details.")
        
        params = {
            "db": "pubmed",
            "id": ",".join(pmids),
            "retmode": "xml",
            "api_key": self.api_key,
        }
        response = requests.get(f"{self.BASE_URL}/efetch.fcgi", params=params)
        response.raise_for_status()
        return response.text

if __name__ == "__main__":
    api = PubMedAPI()
    query = "cancer research"
    papers = api.fetch_papers(query)
    print(f"Fetched papers: {papers}")

    if papers:
        try:
            details = api.fetch_paper_details(papers[:10])
            print("Paper Details (XML):")
            print(details)
        except ValueError as e:
            print(f"Error: {e}")
