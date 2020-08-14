n=int(input())
t1=int(input())
t2=int(input())



def digit(n):
    t=n
    k=0
    while(t!=0):
        r=t%10
        k=k+(r*r)
        t=t//10
    return k
for i in range(t1,t2+1):
    l=digit(i)
    m=1
    while(l>9):
        j=digit(l)
        l=j
        m=m+1
    if m==n:
        print(i)

        
    
    
    
