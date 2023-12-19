# Parse command line arguments
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("test")
args = parser.parse_args()
test = args.test

# Process data
import numpy as np
result = eval(input())
for testcase in result:
	n = testcase['n']
	if (n == 1000):
		ret = testcase['num_queries']
		ret.sort()
		y = np.array(ret)
		print(y[49], y[89], y[98])