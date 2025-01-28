from typing import Dict, List,Any


def extract_non_academic_authors(papers: List[Dict[str, Any]]) -> List[Dict[str, str]]:
    """Identify non-academic authors and their affiliations, and extract necessary fields."""
    filtered_data = []

    # Loop through each paper in the list
    for paper in papers:
        print("Paper structure:", paper)  # Debugging paper structure

        # Check if paper is a dictionary
        if isinstance(paper, dict):
            # Extract the required fields and assign "N.A." if not present
            pubmed_id = paper.get("uid", "N.A.")
            title = paper.get("title", "N.A.")
            pubdate = paper.get("pubdate", "N.A.")
            corresponding_author_email = paper.get("email", "N.A.")

            # Ensure the paper has 'authors' field
            if 'authors' in paper:
                authors = paper['authors']
                non_academic_authors = []
                company_affiliations = []

                for author in authors:
                    print(f"Author: {author}")  # Debugging each author

                    # Check if affiliation is available and not empty
                    affiliation = author.get('affiliation', "")
                    print(f"Affiliation: {affiliation}")  # Debugging affiliation value

                    if "pharma" in affiliation.lower() if affiliation else False:
                        print(f"Non-academic author found: {author['name']} - {affiliation}")  # Debugging non-academic author
                        non_academic_authors.append(author.get("name", "N.A."))
                        company_affiliations.append(affiliation if affiliation else "N.A.")

                # Construct filtered paper details
                filtered_paper = {
                    "PubmedID": pubmed_id,
                    "Title": title,
                    "Publication Date": pubdate,
                    "Non-academic Authors": non_academic_authors if non_academic_authors else "N.A.",
                    "Company Affiliations": company_affiliations if company_affiliations else "N.A.",
                    "Corresponding Author Email": corresponding_author_email,
                }

                # Add the paper to filtered data only if it has non-academic authors
                filtered_data.append(filtered_paper)

        else:
            print(f"Skipping paper: {paper} because it's not a dictionary.")

    print(f"Filtered data: {filtered_data}")  # Debugging filtered data
    return filtered_data
