def isGoodTuple(nums):

if not len(nums):
    return 0

num_list = []
count = 0

for ind in range(1,len(nums)-1):
    num_list = [nums[ind - 1],nums[ind],nums[ind + 1]]
    num_list.sort()
    if num_list[0] != num_list[-1]:
        if (num_list[1] == num_list[0]) | (num_list[1] == num_list[-1]):
            count += 1

return count
