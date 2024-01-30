import requests
from page_parser import parse
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/Dachshund"
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

def get_citations_needed_count():
    """
    Counts the amount of "citation needed" tags on a wikipedia page and returns an integer
    """
    
    citations = soup.find_all(string="citation needed")

    citation_count = []
    for citation in citations:
    
        citation_count.append(citation)
    
    print(f"The amount of citations '{url}' webpage needs is", len(citation_count))

get_citations_needed_count()