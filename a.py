# Question asked by Microsft , uber and Microsoft 
# it can be done in two ways 1. without sorting 2. with sorting


def findtriplet(nums,n):
    res = set()
    nums = sort()
    for i in range(0,n-2):
        for j in range(i+1,n-1):
            for k in range(j+1,n):
                if (nums[i] + nums[j] + nums[k] == 0):
                    res.add((nums[i],nums[j],nums[k]))
    print (list(res))               
    
arr = [1, -2, 1, 0, 5,1,2,3]
n = len(arr)
findtriplet(arr,n)
