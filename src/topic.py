from topicrawdata import TopicRawData
from elements.related_topics import RelatedTopics
from elements.sentiment import Sentiment

class Topic:
    known_elements = [Sentiment, RelatedTopics]

    def __init__(self, string_query):
        self.string_query
        self.elements = {}

    def assemble(self):
        # pull data from online
        topicrawdata = TopicRawData(self.string_query)
        topicrawdata.populate()

        # perform analysis
        for element in known_elements:
            self.elements[element.get_name()] = element.process(topicrawdata)

