# PubMed Research Paper Fetcher

This script will guide you through the setup, usage, and expectations for running the PubMed Research Paper Fetcher program. It utilizes PubMed's API to search for research papers, fetch details such as authors and affiliations, and saves the results to a CSV file.

---

## 1. Setup Instructions

Before running the script, make sure you have the following:

**a) Python 3.x installed on your system**  
Ensure that Python 3.x is installed and accessible via your terminal.

**b) Required dependencies (see requirements below)**  
These dependencies are necessary to run the script.

**c) A valid API key from PubMed**  
You can obtain the API key from [PubMed API Guide](https://www.ncbi.nlm.nih.gov/books/NBK25501/).

### After obtaining the API key, create a `.env` file in the project directory and add the key like so:
PUBMED_API_KEY=your_api_key_here
Example:

PUBMED_API_KEY=123456789abcdefg



**d) Python Packages**  
The script requires the following Python packages:
- `requests`
- `python-dotenv`
- `argparse`

To install them, run:

pip install -r requirements.txt



or

**i. Clone the repository** (if you haven't already):

git clone https://github.com/Aadik1ng/PubMed.git



**ii. Navigate into the project directory**:

cd src\get_papers_list



**Install Poetry:**

For **Windows (PowerShell)** users:

(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | python -



After installing, activate the Poetry environment:

poetry env_name



Make sure you have created a `.env` file with your API key before running the program.

---

## 2. "Running the Script"

Once you have everything set up, you can run the program via the command line using the following format:

get-papers-list 'your_search_query' [options]



**Example:**

get-papers-list 'cancer therapy' --file results.csv



### Arguments:
- `your_search_query`: The query you wish to search for (e.g., "cancer research").
- `-f output.csv` (optional): If you want to save the results to a CSV file, specify the output filename here.
- `-d` (optional): Enable debug output to view detailed API responses and paper structures.

### Help Command
To see all available options, run:

get-papers-list --help



This will display the script's usage instructions, which may look like:

usage: get-papers-list [-h] [-d] [-f FILE] query

Fetch research papers from PubMed.

positional arguments: query Search query.

optional arguments: -h, --help Show this help message and exit. -d, --debug Enable debug output. -f FILE, --file FILE Specify output filename.



---

## 3. "Expected Output"

Once you run the script, the following outcomes are possible:

### No Papers Found
If no papers are found for the given query, you'll see:

No papers found for the query 'your_search_query'.


### No Relevant Non-Academic Authors
If papers are found but no relevant non-academic authors are identified, you'll see:

No detailed papers found.



### Papers Found and Non-Academic Authors Identified
If papers are found and non-academic authors are identified, the following will occur:
- The filtered papers will either be printed to the console or saved to the specified CSV file (if `-f` is provided).
- The CSV will include details like:
  - PubMed ID
  - Title
  - Publication Date
  - Non-academic authors and their affiliations
  - Corresponding author email (if available)

**Example CSV output:**

PubmedID, Title, Publication Date, Non-academic Authors, Company Affiliations, Corresponding Author Email 123456, Research Paper 1, 2023-05-01, John Doe, PharmaCorp, johndoe@pharma.com 789101, Research Paper 2, 2022-11-15, Jane Smith, MedTech Inc., janesmith@medtech.com





## 4. "Troubleshooting and Debugging"

If you're having trouble, check the following:

### Check API Key
Ensure that your `.env` file contains the correct PubMed API key. If it's missing or invalid, you'll get errors when trying to fetch data.

### Debug Mode
If there are issues with the API response, running the script with the `-d` (debug) option will print additional information to help identify issues.

### Empty CSV Output
If the CSV output is empty, check if the program was able to find any non-academic authors in the fetched papers.

### Unexpected Behavior
If you're seeing unexpected behavior, check the response from the PubMed API (this will be printed if `-d` is enabled) to see if the structure matches expectations.

---

## 5. "Code Overview"

The following files and functions are used in the script:

### `api.py`
The main script responsible for fetching paper data from PubMed and processing it.

### `PubMedAPI`
A class used to interact with the PubMed API, responsible for searching and fetching paper details.

### `extract_non_academic_authors`
A function that processes the papers to identify authors from pharmaceutical companies or other non-academic entities.

### `save_to_csv`
A function to save the filtered paper data to a CSV file.

---

## 6. "Final Reminder"

Make sure to include your **own PubMed API key** in the `.env` file before running the script! Without it, the program will not be able to connect to the PubMed API.

**Example:**

PUBMED_API_KEY=your_api_key_here


That's it! You're now ready to fetch and filter research papers from PubMed. Enjoy!

---

# End
