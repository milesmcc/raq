# -*- coding: utf-8 -*-
from rake_nltk import Rake
import string
import pdb
import wolframalpha
import numpy as np
import requests
import unirest
from topia.termextract import extract

class RelatedArticles:
    def __init__(self):
        pass

    def get_name(self):
        return "RelatedArticles"

    def get_human_readable_name(self):
        return "Related Articles"

    def process(self, topicrawdata):
        toparticles = topicrawdata.articles[:5]
        return {
            "top_articles": [{
                "headline": article.get_headline(),
                "thumbnail": article.get_thumbnail(),
                "url": article.get_url()
            } for article in toparticles]
        }
