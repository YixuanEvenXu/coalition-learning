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
xspecial = []
boundspecial = []
for testcase in result:
	n = testcase['n']
	m = testcase['m']
	ret = testcase['num_queries']
	x.append(m)
	y.append(np.mean(ret))
	error.append(np.std(ret))
	bound.append(4.16 * np.log2(n) * n)
	if (m == 1):
		xspecial.append(m)
		boundspecial.append(2 * np.log2(n) * n + 4 * n)
	if (m == n):
		xspecial.append(m)
		boundspecial.append(0.70 * np.log2(n) * n)
		
x = np.array(x)
y = np.array(y)
error = np.array(error)
bound = np.array(bound)
plt.figure(figsize=(9, 4.5))

# Plot Figure 4 (g, h, i)
plt.subplots_adjust(bottom = 0.22, top = 0.96, left = 0.2, right = 0.98)

plt.plot(x, bound, marker='+', markersize=25, markeredgewidth=6, alpha=0.7, linewidth=4, label='Bound')
plt.fill_between(x, y - error, y + error, alpha=0.2, color='orange')
plt.errorbar(x, y, yerr=error, fmt='-x', capsize=6, markersize=25, markeredgewidth = 6, alpha=0.7, linewidth=4, label='AuctionIG')
plt.plot(xspecial, boundspecial, marker='+', markersize=25, markeredgewidth=6, alpha=0.7, linestyle='', label='Special Bound', zorder=5)

plt.xticks(fontsize=28)
plt.yticks(fontsize=28)
plt.ylim(bottom=0)
plt.xlabel('Number of groups (m)', fontsize=28)
plt.ylabel('Sample count', fontsize=28)
if (test == 'D'):
	plt.legend(loc='best', fontsize=28)

plt.savefig(f'figures/{test}1.pdf')
plt.savefig(f'figures/{test}1.png')
plt.clf()