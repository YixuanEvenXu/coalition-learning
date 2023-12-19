# Parse command line arguments
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("test")
args = parser.parse_args()
test = args.test

# Import modules
from items import *
from agents import *
from algorithm import *

if (test in ['A', 'B', 'C']):
	data = [2, 50, 100, 200, 500, 1000]
	if (test == 'A'):
		# Fix m = 1
		data = [(x, 1) for x in data]
	if (test == 'B'):
		# Fix m = n
		data = [(x, x) for x in data]
	if (test == 'C'):
		# Sample m uniformly at random
		data = [(x, -1) for x in data]
		
	# Repeat 100 times
	num_iter = 100
	result = []

	for (n, m) in data:
		num_queries = []
		for i in range(num_iter):
			agents = Agents(n, m)
			items = Items(n)
			algorithm = AuctionIG(n)
			ret = algorithm.main(agents, items)
			assert(agents.check(ret))
			num_queries.append(items.num_used)
		result.append({'n': n, 'num_queries': num_queries})

	print(result)

else:
	data = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
	if (test == 'D'):
		# Fix n = 10
		n = 10
	if (test == 'E'):
		# Fix n = 100
		n = 100
	if (test == 'F'):
		# Fix n = 1000
		n = 1000
	
	# Repeat 100 times
	num_iter = 100
	result = []

	for p in data:
		m = max(int(n * p), 1)
		num_queries = []
		for i in range(num_iter):
			agents = Agents(n, m)
			items = Items(n)
			algorithm = AuctionIG(n)
			ret = algorithm.main(agents, items)
			assert(agents.check(ret))
			num_queries.append(items.num_used)
		result.append({'n': n, 'm': m, 'num_queries': num_queries})
	
	print(result)