import sys

def palindrome(x):
	s = str(x) # int to string
	r = reversed( s ) # r is an iterator
	sr = "".join(r) # join called on empty string ""
	if( s == sr ):
		return True
	else:	
		return False
	
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
	if( len(test) > 0 ):
		n = test.split(' ')
		num = [ int(i) for i in n ]
		#print num
		if( len(num) == 2 ):
			r = num[1]-num[0]+1
			ni = 0
			for i in range(r):
				slen = i+1 # subrange length
				for j in range(r-slen+1): # subrange offset
					np = 0
					for k in range(slen): # iteration over subrange
						if palindrome(num[0]+k+j):
							np += 1
					if( (np % 2) == 0 ):
						ni += 1
						#print num[0]+j, num[0]+j+slen-1
			print ni			
test_cases.close()
