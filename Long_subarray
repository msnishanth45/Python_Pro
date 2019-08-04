def loa(ar, r) : 
	a = 1
	l = 1
	for i in range(1, r) : 
		if (ar[i] > ar[i-1]) : 
			l =l + 1
		else :
			if (a < l) : 
				a = l 
			l = 1
	if (a < l) : 
		a = l 
	return a 

n =int(input()) 
arr =list(map(int,input().split()))
print(loa(arr, n)) 
