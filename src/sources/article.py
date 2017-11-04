import newspaper

class Article:
    def __init__(self, url):
    	self.url = url
    	self.scrape()

    def getText(self):
    	return self.article.text

    def getHeadline(self):
        return self.article.title

    def scrape(self):
        a = newspaper.Article(self.url)
        a.download()
        a.parse()
        self.article = a

