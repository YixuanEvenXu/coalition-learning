class Items:
	# This class is used to generate a list of values of agents
	# Members:
	# n_agents: number of agents
	# num_used: number of items used

	def __init__(self, n_agents):
		# initialize the partition of groups
		# n_agents: number of agents
		self.n_agents = n_agents
		self.num_used = 0

	def item(self):
		# return a list of values of agents
		import random
		self.num_used += 1
		return [random.random() for i in range(self.n_agents)]