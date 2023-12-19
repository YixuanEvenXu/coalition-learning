class AuctionIG:
	# AuctionIG algorithm
	# Members:
	# n_agents: number of agents
	# unionfind: the union-find data structure
	# progress: the progress of binary search of each agent

	def __init__(self, n_agents):
		# initialize the algorithm
		# n_agents: number of agents
		self.n_agents = n_agents
		self.unionfind = [i for i in range(n_agents)]
		self.progress = ['unknown' for i in range(n_agents)]
	
	def find(self, x):
		# find the representative of the group of x
		if (self.unionfind[x] == x):
			return x
		else:
			self.unionfind[x] = self.find(self.unionfind[x])
			return self.unionfind[x]
	
	def query(self, agents, firstmax, secondmax, values, querylist):
		# query if any agent in querylist is cooperating with the agent with firstmax
		# agents: the agents
		# firstmax: the maximum value
		# secondmax: the second maximum value
		# values: a list of values of agents
		# querylist: a list of agents to be queried
		reserves = [firstmax for i in range(self.n_agents)]
		for i in querylist:
			reserves[i] = secondmax
		return agents.auction(values, reserves)
	
	def main(self, agents, items):
		# run the algorithm
		# agents: the agents
		# items: the items
		import random

		# the outer while loop
		while (self.progress.count('finished') < self.n_agents - 1):
			# Get the values of the next item
			values = items.item()
			
			# Find the maximum and the second maximum
			maxpos = 0
			firstmax = 0
			secondmax = 0
			for i in range(self.n_agents):
				if (values[i] > firstmax):
					secondmax = firstmax
					firstmax = values[i]
					maxpos = i
				elif (values[i] > secondmax):
					secondmax = values[i]
			
			# Check if we can proceed the binary search of maxpos with this item
			rootx = self.find(maxpos)
			if (firstmax == secondmax or self.progress[rootx] == 'finished'):
				continue

			# Proceed the binary search of maxpos with this item
			if (self.progress[rootx] == 'unknown'):
				querylist = []
				for i in range(self.n_agents):
					if (self.progress[i] != 'finished' and i != rootx):
						querylist.append(i)
				if (self.query(agents, firstmax, secondmax, values, querylist)):
					self.progress[rootx] = 'finished'
				elif (len(querylist) == 1):
					rooty = self.find(querylist[0])
					valid = False
					if (self.progress[rooty] != 'unknown'):
						valid = True
						for x in self.progress[rooty]:
							if (self.find(x) == rootx):
								valid = False
								break
					if (valid):
						self.progress[rootx] = self.progress[rooty]
					else:
						self.progress[rootx] = 'unknown'
					self.progress[rooty] = 'finished'
					self.unionfind[rooty] = rootx
				else:
					self.progress[rootx] = querylist
			else:
				random.shuffle(self.progress[rootx])
				querylist = self.progress[rootx][0:len(self.progress[rootx]) // 2]
				if (self.query(agents, firstmax, secondmax, values, querylist)):
					self.progress[rootx] = self.progress[rootx][len(self.progress[rootx]) // 2:]
				else:
					self.progress[rootx] = querylist
				if (len(self.progress[rootx]) == 1):
					rooty = self.find(self.progress[rootx][0])
					valid = False
					if (self.progress[rooty] != 'unknown'):
						valid = True
						for x in self.progress[rooty]:
							if (self.find(x) == rootx):
								valid = False
								break
					if (valid):
						self.progress[rootx] = self.progress[rooty]
					else:
						self.progress[rootx] = 'unknown'
					self.progress[rooty] = 'finished'
					self.unionfind[rooty] = rootx
		
		# Return the result
		ret = []
		for i in range(self.n_agents):
			if (self.unionfind[i] != i):
				continue
			thisgroup = []
			for j in range(self.n_agents):
				if (self.find(j) == i):
					thisgroup.append(j)
			ret.append(thisgroup)
		return ret