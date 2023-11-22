import argparse
import json
from datetime import datetime
import requests


API_KEY = "bf27ff5d980a489b8c86d591c416819e"
URL = "https://newsapi.org/v2/everything?q={query}&from={date}&searchin={section}&apiKey={api_key}"

class SearchParameters:
    query: str
    date: datetime
    section: list[str]
    key: str
    search_url: str

    def __init__(self, 
                 query: list[str], 
                 date: str, 
                 section: list[str], 
                 key: str,
                 format: str):

        self.query = '&'.join(query)
        self.date = datetime(*[int(x) for x in date.split('-')])
        self.section = section
        self.key = key
        self.format_url(format)

    def __str__(self):
        return self.search_url

    def format_url(self, format_url):
        self.search_url = format_url.format(query=self.query, 
                                            date=self.date.date(), 
                                            section=','.join(self.section),
                                            api_key=self.key)



def get_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog="News Articles Fetcher",
        description="Search for news articles using newsapi.org"
    )
    
    parser.add_argument('-o', '--output')
    parser.add_argument('-u', '--url', action="store_true")
    parser.add_argument('-q', '--query', 
                        required=True, 
                        nargs='*')
    parser.add_argument('-s', '--section', 
                        choices=["title", "content", "description"], 
                        default=["title", "content", "description"],
                        nargs='*')
    parser.add_argument('-d', '--date',
                        default="2023-10-22")
    return parser.parse_args()
    

def main():

    args = get_args();

    search_params = SearchParameters(args.query,
                                     args.date, 
                                     list(set(args.section)),   # de-duplicate sections 
                                     API_KEY, 
                                     URL)

    # contact api
    response = requests.get(str(search_params))
    data = response.json()
    
    if args.url:
        print('URL', search_params)

    if args.output:
        with open(args.output, 'w') as f:
            json.dump(data, f, indent=2)
    else:
        print(json.dumps(data, indent=2))


if __name__ == "__main__":
    main()
