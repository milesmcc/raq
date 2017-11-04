class Sentiment:
    __init__(self):
        pass

    def get_name():
        return "Sentiment"

    def get_human_readable_name():
        return "Sentiment Score"

    """
    strings: an array of strings on which to do the data analysis
    """
    def process(self, topicrawdata):

        strings = topicrawdata.get_strings()

        # return your list of related topic strings here
        return {
            "sentiment": -0.3
        }
