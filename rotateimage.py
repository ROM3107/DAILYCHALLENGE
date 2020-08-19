import numpy as np
def rotateImage(a):
   
    a=np.array(a)
    a=a.transpose()
    a=a.tolist()
    for i in range(0,len(a)):
        a[i].reverse()
    
    return a
    

