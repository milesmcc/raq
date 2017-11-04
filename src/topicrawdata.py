class TopicRawData:
    '''get the raw data from a lot of sources and put it into a '''
    def __init__(self, topicstring):
        self.topicstring = topicstring

        self.tweets = None # array of tweets, according to Twitter's specification
        self.articles = None # array of article classes
        self.wikipedia = None # array of Wikipedia classes
        self.reddit = None # array of Reddit comments

    def populate(self):
        pass
        # fetch raw data

    def strings(self):
        # return all strings

        return self.articles.getAllString()# + self.[source].getAllStrings() for other sources

    def getArticles(self): # the only one we're using rn
        return self.articles

    # getters for tweets, wikipedia, reddit, etc
