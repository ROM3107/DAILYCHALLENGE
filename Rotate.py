def rotate(nums, k):
        l=[]
        q=[]
        m=[]
        for i in range(k+1,len(nums)):
            l.append(nums[i])
        for j in range(0,k+1):
            q.append(nums[j])
        m=l+q
        return m
a=[1,2,3,4,5,6,7]
d=3
g=rotate(a,d)
print(g)
