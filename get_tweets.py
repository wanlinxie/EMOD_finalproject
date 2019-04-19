#from twitter import *
import requests
import json
import csv

#  consumer_key="usD0gscQSZtHiiCS0dkZ3fC8k"
#  consumer_secret="86KtIBElRcntd95Ld2BbVTFXF6xDIxXEuft1UlgwupK8vN43g6"
#  access_token_key="1110926321469849600-SXmqDT5m6Xv1v565PN7d1PHt68H4Vp"
#  access_token_secret="Zoyp7k5o6asg1FfsVxup8OCXImEHzs42fr2zDRI9pgYRp"


#{"token_type":"bearer","access_token":"AAAAAAAAAAAAAAAAAAAAAI7f9gAAAAAAQ%2BphMLjBfkuHtia%2FV%2FvJa44%2FDj4%3Dze44FuRic5YleyQMQZ4q8ngDGsSl0yqKrXbjc02UIykAawTYny"}

endpoint = "https://api.twitter.com/1.1/tweets/search/30day/production.json"

headers = {"Authorization":"Bearer AAAAAAAAAAAAAAAAAAAAAI7f9gAAAAAAQ%2BphMLjBfkuHtia%2FV%2FvJa44%2FDj4%3Dze44FuRic5YleyQMQZ4q8ngDGsSl0yqKrXbjc02UIykAawTYny", "Content-Type": "application/json"}  

data = '{"query":"tesla lang:en", "fromDate": "201903020000", "toDate": "201904010000", "maxResults":100},'

response = requests.post(endpoint,data=data,headers=headers).json()


#print(json.dumps(response, indent = 2))
tweets = []
for res in response['results']:
    date = res['created_at']
    text = res['text']
    tweets.append([date, text])

with open('tweets.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerows(tweets)

#t = Twitter(
#      auth=OAuth(
 #      "1110926321469849600-SXmqDT5m6Xv1v565PN7d1PHt68H4Vp", 
 #      "Zoyp7k5o6asg1FfsVxup8OCXImEHzs42fr2zDRI9pgYRp",
 #      "usD0gscQSZtHiiCS0dkZ3fC8k",
 #      "86KtIBElRcntd95Ld2BbVTFXF6xDIxXEuft1UlgwupK8vN43g6"))

#search_word = "snapchat"

#tweets = t.search.tweets(q=search_word, 
#	count=100)

#raw_data = json.dumps(tweets)
#data = json.loads(raw_data)

#for k,v in data.items():
#	print(k)

#with open(search_word+"_data.json","w") as fp:
#    json.dump(data, fp)

