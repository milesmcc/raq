from __future__ import print_function
from .topic import Topic
import json

class Manager:
	def __init__(self):
		self.topic_path = []

	def get_graph_json(self, querystring):
		graph = []
		root_topic = Topic(querystring)
		self.topic_path.append(root_topic)
		graph.append(root_topic.assemble())
		for related_level1 in root_topic.get_related_topics():
			topic_level1 = Topic(related_level1)
			graph.append(topic_level1.assemble())
			for related_level2 in topic_level1.get_related_topics():
				topic_level2 = Topic(related_level1)
				graph.append(topic_level2.assemble())
		for topic in self.topic_path[-min(len(self.topic_path), 3):]:
			graph.append(topic.assemble())
		graph = {v['name']:v for v in map(lambda x: x, graph)}.values()
		for thing in graph:
			print(thing)
		graph_json = json.dumps(graph)
		# print "\n\n"
		# print graph
		# print "\n"
		return graph_json
		# dummy data:
		# s = '''[
		# 	{
		# 		"name": "a"
		# 		"elements": {
		# 			"RelatedTopics": ["one", "two", "three"],
		# 			"Sentiment": {
		# 				"sentiment": 0.5,
		# 				"individual_sentiments": [0.1, 0.2, 0.3]
		# 			}
		# 		}
		# 	},
		# 	{
		# 		"name": "b"
		# 		"elements": {
		# 			"RelatedTopics": ["a", "five", "six"],
		# 			"Sentiment": {
		# 				"sentiment": 0.5,
		# 				"individual_sentiments": [0.1, 0.2, 0.3]
		# 			}
		# 		}
		# 	},
		# 	{
		# 		"name": "c"
		# 		"elements": {
		# 			"RelatedTopics": ["a", "seven", "eight"],
		# 			"Sentiment": {
		# 				"sentiment": 0.5,
		# 				"individual_sentiments": [0.1, 0.2, 0.3]
		# 			}
		# 		}
		# 	}
		# ]'''
		# s = s.replace("\n", "")
		# return s

if __name__ == "__main__":
	m = Manager()
	print(m.get_graph_json("kaspersky"))