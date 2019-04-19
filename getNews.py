#!/usr/bin/env python3
#Get news articles URLs

#companies: Tesla(TSLA), Facebook(FB), Boeing(BA), Netflix(NFLX)
#news sources: "marketwatch.com, businessinsider.com, yahoo.com"
#csv fields = [date, title, url]
import csv
from newsapi import NewsApiClient
#companies = ['Tesla','Facebook','Snapchat','Google','Nvidia']
newsapi = NewsApiClient(api_key= "4a4a6e7c05cb46c3bd7a665f7df5eea1")
sources = newsapi.get_sources()


for c in ['TSLA','FB','BA','NFLX']:
    for domain in ['marketwatch.com','businessinsider.com','yahoo.com']:
    #for domain in ['finance.yahoo.com']:
        urls = []
        all_articles = newsapi.get_everything(q=c,
                                              #sources='the-wall-street-journal',
                                              #domains = "yahoo.com",
                                              domains = domain,
                                              #domains = 'businessinsider.com',
                                              from_param='2019-04-11',
                                              to='2019-04-18',
                                              language='en',
                                              sort_by='relevancy',
                                              page_size=100,
                                              page=1)
        articles = all_articles['articles']

# remain = newsapi.get_everything(q=c,
#                                 from_param='2019-03-03',
#                                 to='2019-04-03',
#                                 language='en',
#                                 sort_by='relevancy',
#                                 page_size=120 - num,
#                                 page=1)
# for aa in remain['articles']:
#     if aa in articles:
#         continue
#     else:
#         articles.append(aa)
        for article in articles:
            urls.append([article['publishedAt'][:10], article['title'],article['url']])

        with open(c + "_" + domain + '_prediction.csv','w') as f:
            csvwriter = csv.writer(f)
            csvwriter.writerows(urls)