def commonPrefixUtil(str1, str2): 

	result = ""; 
	n11 = len(str1) 
	n22 = len(str2) 
	i = 0
	j = 0
	while i <= n11 - 1 and j <= n22 - 1: 
	
		if (str1[i] != str2[j]): 
			break
			
		result += str1[i] 
		i += 1
		j += 1

	return (result) 

def commonPrefix (arr, n): 

	prefix = arr[0] 

	for i in range (1, n): 
		prefix = commonPrefixUtil(prefix, arr[i]) 

	return (prefix) 


n=int(input())
arr =[]
for i in range(0,n):
  l = input()
  arr.append(l)
ans = commonPrefix(arr, n) 

if (len(ans)): 
	print (ans);
