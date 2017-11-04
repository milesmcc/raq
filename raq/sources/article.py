import eatiht

class Article:
    def __init__(self, url, headline):
    	self.url = url
        self.headline = headline
    	self.scrape()

    def get_text(self):
    	return self.text

    def get_thumbnail(self):
        if "thumbnail" in self:
            return self.thumbnail
        else:
            return None

    def get_url(self):
        return self.url

    def get_headline(self):
        return self.headline

    def scrape(self):
        self.text = eatiht.extract(self.url)
