x=int(input())
y=list(map(int,input().split()))[0:x]
y.sort(reverse=True)
i=0
while i<x:
    print(y[i],end="\n")
    i+=1
