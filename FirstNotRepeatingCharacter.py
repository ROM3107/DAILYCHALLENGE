def firstNotRepeatingCharacter(s):
    k="_"
    l=set(s)
    p=[]
    r=list(l)
    m=len(s)
    for i in range(0,len(r)):
        if s.count(r[i])==1:
            p.append(s.find(r[i]))
   
            
    if len(p)==0:
        return k
    else:
        return s[min(p)]

