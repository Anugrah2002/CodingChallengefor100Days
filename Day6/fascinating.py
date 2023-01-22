def fascinating(self,n):
	# code here
	lis = '123456789'
	c = n*2
	d = n*3
	n = str(n)+str(c)+str(d)
	n =''.join(sorted(n))
	if n == lis:
		return True
	else:
		return False