t= "aaabbccde"
s=''
b=set(t)
d=str(b)
res = ''.join(sorted(b)) 
for a in res:
    l=t.count(a)
    if l ==1:
        s=s+a
        continue
    else:
        s=s+a+str(l)
print(s)
