class Agents:
	# This is a class used to maintain a partition of agents into groups
	# Memebers:
	# n_agents: number of agents
	# n_groups: number of groups
	# groups: a list of lists, each list is a group
	# belong: a list of integers, each integer is the group number of the corresponding agent

	def __init__(self, n_agents, n_groups = -1): 
		# initialize the partition of groups
		# n_agents: number of agents
		# n_groups: number of groups (-1 means that the number of groups is random)
		import random
		if n_groups == -1:
			n_groups = random.randint(1, n_agents)
		self.n_agents = n_agents
		self.n_groups = n_groups

		rename = [i for i in range(n_agents)]
		random.shuffle(rename)
		self.groups = []
		for i in range(n_groups):
			self.groups.append([rename[i]])
		for i in range(n_groups, n_agents):
			self.groups[random.randint(0, n_groups - 1)].append(rename[i])
		for i in range(n_groups):
			self.groups[i].sort()
		self.groups.sort()
		
		self.belong = [0 for i in range(n_agents)]
		for i in range(n_groups):
			for j in self.groups[i]:
				self.belong[j] = i
	
	def __str__(self):
		# print the partition of groups
		return str(self.groups)
	
	def auction(self, values, reserves):
		# check if bidding truthfully is a nash equilibrium
		# values: a list of values of agents
		# reserves: a list of reserves of agents
		maxvalues = [0 for i in range(self.n_groups)]
		for i in range(self.n_agents):
			maxvalues[self.belong[i]] = max(maxvalues[self.belong[i]], values[i])
		
		firstmax = 0
		secondmax = 0
		for i in range(self.n_groups):
			if (maxvalues[i] > firstmax):
				secondmax = firstmax
				firstmax = maxvalues[i]
			elif (maxvalues[i] > secondmax):
				secondmax = maxvalues[i]
		
		for i in range(self.n_agents):
			if (maxvalues[self.belong[i]] == firstmax):
				outsidemax = secondmax
			else:
				outsidemax = firstmax
			payment = max(reserves[i], outsidemax)
			if (maxvalues[self.belong[i]] > payment):
				return False
		
		return True
	
	def check(self, predicted_groups):
		# check if the predicted groups are the same as the true groups
		# predicted_groups: a list of lists, each list is a group
		if len(predicted_groups) != self.n_groups:
			return False
		
		for i in range(self.n_groups):
			predicted_groups[i].sort()
		predicted_groups.sort()
		
		return predicted_groups == self.groups