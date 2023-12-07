from newsapi import NewsApiClient
import json
# Init
newsapi = NewsApiClient(api_key='39c9bdc004d9478796169d90f905889f')

# /v2/top-headlines
# top_headlines = newsapi.get_top_headlines(q='Marvels+Napoleon',
#                                           category='entertainment',
#                                           language='en',
#                                           page_size=100
#                                        )

# # /v2/everything
all_articles = newsapi.get_everything(q='Marvels OR Napoleon OR (Five AND nights AND at AND Freddys) OR (Hunger AND Games)',
                                      from_param='2023-11-06',
                                      to='2023-12-06',
                                      language='en',
                                      sort_by='relevancy'
)

# /v2/top-headlines/sources
#sources = newsapi.get_sources()

with open('relevant_news_articles.json', 'w') as f:
            json.dump(all_articles, f, indent=2)