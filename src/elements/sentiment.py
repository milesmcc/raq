from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


class Sentiment:
    def __init__(self):
        pass

    def get_name():
        return "Sentiment"

    """
    strings: an array of strings on which to do the data analysis
    """
    def process(self, topicdata):

        strings = topicdata.strings()
        scores = [self.process_string(string) for string in strings]
        total_score = self.process_string(' '.join(strings))

        # return your list of related topic strings here
        return {
            "sentiment": total_score,
            "individual_sentiments": scores
        }

    def process_string(self, text):
        """Returns a simple compound score for a piece of text."""
        analyzer = SentimentIntensityAnalyzer()
        return analyzer.polarity_scores(text)["compound"]
