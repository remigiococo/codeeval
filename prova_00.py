import sys
import string

def primes_until(x):
	pr = set( [2] )
	for i in xrange(3,x+1):
		isp = 1
		for j in pr:
			if (i % j) == 0:
				isp = 0
		if isp == 1:
			pr.add( i )
	return pr

n = 4	
pri = primes_until(n*2)
sums = [ [j for j in xrange(1, n+1) if i+j in pri] for i in xrange(n+1)]
prod = 1
for x in sums[1:]:
	print len(x), x
	prod *= len(x)
print "---", prod

nck = [1]
for i in xrange(1, n):
	cur = nck[i-1]
	for x in sums[cur]:
		if x not in nck:
			nck.append(x)
			break
if nck[n-1]+nck[0] in pri:			
	print nck