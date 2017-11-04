class TopicData:
    def __init__(self, topicstring):
        self.topicstring = topicstring

        self.tweets = None # array of tweets, according to Twitter's specification
        self.articles = None # array of article classes
        self.wikipedia = None # array of Wikipedia classes
        self.reddit = None # array of Reddit comments

    def populate(self):
        pass
        # fetch all data

    def strings(self):
        pass
        # return all strings
