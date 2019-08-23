import sys

mil = { 1 : 'M', 2 : 'MM', 3 : 'MMM' }
cen = { 1 : 'C', 2 : 'CC', 3 : 'CCC', 4 : 'CD', 5 : 'D', 6 : 'DC' , 7 : 'DCC', 8 : 'DCCC', 9 : 'CM' }
dec = { 1 : 'X', 2 : 'XX', 3 : 'XXX', 4 : 'XL', 5 : 'L', 6 : 'LX' , 7 : 'LXX', 8 : 'LXXX', 9 : 'XC' }
uni = { 1 : 'I', 2 : 'II', 3 : 'III', 4 : 'IV', 5 : 'V', 6 : 'VI' , 7 : 'VII', 8 : 'VIII', 9 : 'IX' }

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
	if( len(test) > 0 ):
		n = int(test)
		m = n / 1000
		n -= (m * 1000)
		c = n / 100
		n -= (c * 100)
		d = n / 10
		n -= (d * 10)
		#print m, c, d, n
		s = ""
		if m > 0:
			s += mil[m]
		if c > 0:
			s += cen[c]
		if d > 0:
			s += dec[d]
		if n > 0:	
			s += uni[n]
		print s	
test_cases.close()