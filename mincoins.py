import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
	if( len(test) > 0 ):
		n = int(test)
		i = 0
		while( n >=5 ):
			n -= 5
			i += 1
		while( n >=3 ):
			n -= 3
			i += 1
		i += n
		print i		
test_cases.close()
