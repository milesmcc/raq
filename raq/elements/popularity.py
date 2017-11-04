# -*- coding: utf-8 -*-
from rake_nltk import Rake
import string
import pdb
import wolframalpha
import numpy as np
import requests
import unirest
from topia.termextract import extract

class Popularity:
    def __init__(self):
        pass

    def get_name(self):
        return "Popularity"

    def get_human_readable_name(self):
        return "Popularity (Mentions)"

    def process(self, topicrawdata):
        return {
            "popularity": topicrawdata.search_results
        }
