import json
import urllib
import requests

class TopicRawData:
    '''get the raw data from a lot of sources and put it into a '''
    def __init__(self, topicstring):
        self.topicstring = topicstring
        self.articles = [] # array of article classes

        self.subscriptionKey = secret = open('../secrets.txt').readlines()[3]

    def populate(self):
        host = "https://api.cognitive.microsoft.com/bing/v7.0/search"
        headers = {'Ocp-Apim-Subscription-Key': self.subscriptionKey}
        response = requests.get(host + "?q=" + self.topicstring + "&searchFilters=News", headers=headers).json()


    def strings(self):
        # return all strings
        allthestrings = []
        for article in self.articles:
            allthestrings.append(article.get_text())
        return allthestrings

    def getArticles(self): # the only one we're using rn
        return self.articles

    # getters for tweets, wikipedia, reddit, etc
