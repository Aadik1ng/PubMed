import csv
from typing import List, Dict

def save_to_csv(data: List[Dict[str, str]], filename: str) -> None:
    """Save results to a CSV file."""
    # Debugging: Check the content of data before saving
    print(f"Data to be saved: {data}")
    
    if data:  # Only save if data is not empty
        with open(filename, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=["PubmedID", "Title", "Publication Date", "Non-academic Authors", "Company Affiliations", "Corresponding Author Email"])
            writer.writeheader()
            writer.writerows(data)
    else:
        print("No data to save.")

