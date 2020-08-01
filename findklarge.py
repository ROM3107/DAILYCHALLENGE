
l=list(map(int,input().strip().split()))
k=int(input())
m=[]
l.sort(reverse=True)
if k>len(l):
    print("0")
else:
    for i in range(0,k):
        m.append(l[i])
    print (m)
    
