def delivery(order, shoppers):
    l=[]
    d=order[0]
    l1=order[1]
    l2=order[2]
    j=0
    for i in range(0,len(shoppers)):
        j=shoppers[i][0]+d
        m=j/shoppers[i][1]
        k=m+shoppers[i][2]
        if (k>=l1 and k<=l2+l1):
            l.append(True)
        else:
            l.append(False)
    return l



