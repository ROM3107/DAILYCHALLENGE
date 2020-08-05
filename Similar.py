def areSimilar(a, b):
    if a==b: return True
    l = [i for i in list(zip(a,b)) if i[0]!=i[1]]
    if len(l)==2 and l[0][1] == l[1][0] and l[0][0] == l[1][1]: return True
    return False
