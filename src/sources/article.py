# import newspaper

class Article:
    def __init__(self, url):
    	self.url = url
    	# self.scrape()

    def get_text(self):
        #temp
        return '''heres some dummy article text'''
    	# return self.article.text

    def get_headline(self):
        return self.article.title

    def scrape(self):
        a = newspaper.Article(self.url)
        a.download()
        a.parse()
        self.article = a

