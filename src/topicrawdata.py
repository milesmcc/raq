class TopicRawData:
    '''get the raw data from a lot of sources and put it into a '''
    def __init__(self, topicstring):
        self.topicstring = topicstring

        self.tweets = None # array of tweets, according to Twitter's specification
        self.articles = None # array of article classes
        self.wikipedia = None # array of Wikipedia classes
        self.reddit = None # array of Reddit comments

        subscriptionKey =

    def populate(self):
        pass
        # fetch raw data

    def strings(self):
        # return all strings
        allthestrings = ""
        for article in self.articles:
            allthestrings += article.getContent()
        return allthestrings

    def getArticles(self): # the only one we're using rn
        return self.articles

    # getters for tweets, wikipedia, reddit, etc
