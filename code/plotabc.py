# Parse command line arguments
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("test")
args = parser.parse_args()
test = args.test

# Import modules
import numpy as np
import matplotlib.pyplot as plt

# Input data
result = eval(input())
x = []
y = []
bound = []
error = []
for testcase in result:
	n = testcase['n']
	ret = testcase['num_queries']
	x.append(n)
	y.append(np.mean(ret))
	error.append(np.std(ret))
	if (test == 'A'):
		bound.append(2 * np.log2(n) * n + 4 * n)
	if (test == 'B'):
		bound.append(0.70 * np.log2(n) * n)
	if (test == 'C'):
		bound.append(4.16 * np.log2(n) * n)

x = np.array(x)
y = np.array(y)
error = np.array(error)
bound = np.array(bound)

# Plot Figure 4 (a, b, c)
plt.figure(figsize=(9, 4.5))
plt.subplots_adjust(bottom = 0.22, top = 0.96, left = 0.20, right = 0.98)

plt.plot(x, bound, marker='+', markersize=25, markeredgewidth=6, alpha=0.7, linewidth=4, label='Bound', zorder=5)
plt.fill_between(x, y - error, y + error, alpha=0.2, color='orange')
plt.errorbar(x, y, yerr=error, fmt='-x', capsize=6, markersize=25, markeredgewidth=6, alpha=0.7, linewidth=4, label='AuctionIG')

plt.xticks(fontsize=28)
plt.yticks(fontsize=28)
plt.xlabel('Number of agents (n)', fontsize=28)
plt.ylabel('Sample count', fontsize=28)
if (test == 'A'):
	plt.legend(loc='best', fontsize=28)

plt.savefig(f'figures/{test}1.pdf')
plt.savefig(f'figures/{test}1.png')
plt.clf()

# Plot Figure 4 (d, e, f)
plt.figure(figsize=(9, 4.5))
plt.subplots_adjust(bottom = 0.22, top = 0.96, left = 0.20, right = 0.98)

for testcase in result:
	n = testcase['n']
	if (n not in [2, 200, 1000]):
		continue
	ret = testcase['num_queries']
	ret.sort()
	x = np.arange(1, len(ret) + 1) / len(ret)
	y = np.array(ret)
	plt.plot(x, y, alpha=0.7, linewidth=4, label=f'N = {n}')

plt.xticks(fontsize=28)
plt.yticks(fontsize=28)
plt.xlabel('Quantile', fontsize=28)
plt.ylabel('Sample count', fontsize=28)
if (test == 'A'):
	plt.legend(loc='upper left', fontsize=28)

plt.savefig(f'figures/{test}2.pdf')
plt.savefig(f'figures/{test}2.png')
plt.clf()