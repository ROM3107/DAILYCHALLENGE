def domainType(domains):
    d=[]
    for i in range(0,len(domains)):
        k=domains[i].rindex(".")
        l=domains[i][k:len(domains[i])]
        if l==".info":
            d.append("information")
        elif l==".com":
            d.append("commercial")
        elif l==".net":
            d.append("network")
        else:
            d.append("organization")
    return (d)
            

