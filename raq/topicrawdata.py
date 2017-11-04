import requests
from sources.article import Article
import os
import json

secrets = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../secrets.txt")

class TopicRawData:
    '''get the raw data from a lot of sources and put it into a '''
    def __init__(self, topicstring):
        self.topicstring = topicstring
        self.articles = [] # array of article classes
        self.search_results = None

        self.subscriptionKey = secret = open(secrets).readlines()[3]

    def populate(self):
        print("Populating: " + self.topicstring)
        host = "https://api.cognitive.microsoft.com/bing/v7.0/news"
        headers = {'Ocp-Apim-Subscription-Key': self.subscriptionKey.strip()}
        response = requests.get(host + "?q=" + self.topicstring + "&searchFilters=News", headers=headers).json()
        for article in response["value"][:4]:
            try:
                articleObj = Article(article["url"], article["name"])
                articleObj.thumbnail = article["image"]["thumbnail"]["contentUrl"]
                self.articles.append(articleObj)
            except:
                print("ERROR ON " + article["url"])
        #print json.dumps(response)
        self.search_results = len(response["value"])

    def strings(self):
        # return all strings
        allthestrings = []
        for article in self.articles:
            allthestrings.append(article.get_text())
        return allthestrings

    def getArticles(self): # the only one we're using rn
        return self.articles

    # getters for tweets, wikipedia, reddit, etc
