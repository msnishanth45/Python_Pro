NO_OF_CHARS = 256
def lS(s): 
    n = len(s) 
    cur_len = 1       
    max_len = 1       
    prev_index = 0  
    i = 0
    v = [-1] * NO_OF_CHARS 
    v[ord(s[0])] = 0
    for i in range(1, n): 
        prev_index =v[ord(s[i])] 
        if prev_index == -1 or (i - cur_len > prev_index): 
            cur_len+= 1
        else: 
            if cur_len > max_len: 
                max_len = cur_len 
  
            cur_len = i - prev_index 
        v[ord(s[i])] = i 
    if cur_len > max_len: 
        max_len = cur_len 
    return max_len 

s = input()
lgth = lS(s) 
print ( str(lgth)) 
