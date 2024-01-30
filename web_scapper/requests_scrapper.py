import requests
from page_parser import parse
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/Dachshund"
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

def get_citations_needed_count():
    """
    Counts the amount of "citation needed" tags on a wikipedia page

    Param: 
        url string

    Output:
        Integer
    """
    
    citations = soup.find_all(string="citation needed")

    citation_count = []
    for citation in citations:
    
        citation_count.append(citation)
    
    print(f"The amount of citations '{url}' needs is {len(citation_count)}.")

get_citations_needed_count()

def get_citations_needed_report():

    # Used ChatGPT to figure out the CSS selector
    citation_reference = soup.select('a[href="/wiki/Wikipedia:Citation_needed"][title="Wikipedia:Citation needed"]')

    for citation_text in citation_reference:
        parent_tag = citation_text.find_parent('p')
        if parent_tag:
            print(parent_tag.text)
        else:
            print("No citation needed tags found")

get_citations_needed_report()