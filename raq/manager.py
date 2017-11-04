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
		searched = [querystring]
		for related_level1 in root_topic.get_related_topics()[:4]:
			if related_level1 in searched:
				continue
			else:
				searched.append(related_level1)
			topic_level1 = Topic(related_level1)
			for related_level2 in topic_level1.get_related_topics()[:4]:
				if related_level2 in searched:
					continue
				else:
					searched.append(related_level2)
				topic_level2 = Topic(related_level1)
				topic_level2.connect(topic_level1.string_query)
				topic_level1.connect(topic_level2.string_query)
				graph.append(topic_level2.assemble())
			graph.append(topic_level1.assemble())
		# for topic in self.topic_path[-min(len(self.topic_path), 3):]:
		# 	graph.append(topic.assemble())
		# graph = {
		# 	v['name']:v for v in map(lambda x: x, graph)
		# }.values()
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
		# 		"name": "a",
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


def think(topic):
	return Manager().get_graph_json(topic)

if __name__ == "__main__":
	m = Manager()
	print(m.get_graph_json("kevin spacey"))