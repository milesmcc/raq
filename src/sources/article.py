class Article:
    def __init__(self, url):
    	self.url = url
    	self.scrape()

    def getText(self):
    	return self.content

    def scrape(self):
    	pass

