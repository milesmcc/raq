from topicrawdata import TopicRawData
from elements.related_topics import RelatedTopics
from elements.sentiment import Sentiment

class Topic:
    '''return dict of relevant info about a single topic'''

    def __init__(self, string_query):
        self.string_query
        self.elements = {}
        self.known_analyses = [Sentiment(), RelatedTopics()]

    def get_related_topics(self):
        return self.elements["RelatedTopics"]["related_topics"]

    def assemble(self):
        # pull data from online
        topicrawdata = TopicRawData(self.string_query)
        topicrawdata.populate()

        # perform analysis
        for analysis in self.known_analyses:
            self.elements[analysis.get_name()] = analysis.process(topicrawdata)

        return {
            "elements": self.elements,
            "name": self.string_query,
        }

    def __eq__(self, other):
        return other.string_query.lower == self.string_query.lower