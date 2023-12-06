from newsapi import NewsApiClient
import json
# Init
newsapi = NewsApiClient(api_key='39c9bdc004d9478796169d90f905889f')

# /v2/top-headlines
top_headlines = newsapi.get_top_headlines(category='entertainment',
                                          language='en',
                                          from_param='2023-11-02',
                                        to='2023-12-01')

# # /v2/everything
# all_articles = newsapi.get_everything(q='Napoleon',
#                                       sources='bbc-news,the-verge',
#                                       domains='bbc.co.uk,techcrunch.com',
#                                       from_param='2023-11-02',
#                                       to='2023-12-01',
#                                       language='en',
#                                       sort_by='relevancy',
#                                       page=2)

# /v2/top-headlines/sources
sources = newsapi.get_sources()

json.dump(top_headlines, open('top_headlines.json', 'w'))