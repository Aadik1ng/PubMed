import requests
from typing import List, Dict, Any


class PubMedAPI:
    BASE_URL_SEARCH = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
    BASE_URL_FETCH = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi"

    def __init__(self, api_key: str):
        self.api_key = api_key

    def fetch_papers(self, query: str) -> List[str]:
        """Fetch paper IDs using the provided query."""
        params = {
            "db": "pubmed",
            "term": query,
            "retmode": "json",
            "retmax": 100,  # Adjust as needed
            "api_key": self.api_key,
        }
        response = requests.get(self.BASE_URL_SEARCH, params=params)
        response.raise_for_status()
        result = response.json()
        paper_ids = result.get("esearchresult", {}).get("idlist", [])
        return paper_ids

    def fetch_paper_details(self, paper_ids: List[str]) -> List[Dict[str, Any]]:
        """Fetch detailed paper information by ID."""
        if not paper_ids:
            return []
            
        params = {
            "db": "pubmed",
            "id": ",".join(paper_ids),
            "retmode": "json",
            "api_key": self.api_key,
        }
        response = requests.get(self.BASE_URL_FETCH, params=params)
        response.raise_for_status()
        result = response.json()

        # Debug: Print the full response structure
        print("Full response:", result)

        # Check if 'result' contains the expected structure (a dictionary of papers)
        if 'result' in result:
            papers = result['result']
            # We need to ensure it's not a list but a dictionary of papers
            if isinstance(papers, dict):
                return list(papers.values())
            else:
                print("Unexpected structure for papers:", papers)
        return []