from topic import Topic

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
			graph.append(topic)
		graph = list(set(graph))
		graph_json = json.dumps(graph)
		return graph_json
