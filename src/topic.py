from topicrawdata import TopicRawData
from elements.related_topics import RelatedTopics
from elements.sentiment import Sentiment

class Topic:
    '''return dict of relevant info about a single topic'''
    known_analyses = [Sentiment, RelatedTopics]

    def __init__(self, string_query):
        self.string_query
        self.elements = {}

    def assemble(self):
        # pull data from online
        topicrawdata = TopicRawData(self.string_query)
        topicrawdata.populate()

        # perform analysis
        for analysis in known_analyses:
            self.elements[analysis.get_name()] = analysis.process(topicrawdata)

        self.elements['uid'] = makeUID()
        self.elements['name'] = self.string_query

        return self.elements