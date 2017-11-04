import newspaper

class Article:
    def __init__(self, url):
    	self.url = url
    	self.scrape()

    def getText(self):
    	return self.content

    def scrape(self):
        a = newspaper.Article(self.url)
        a.download()
        
