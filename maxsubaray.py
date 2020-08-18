class Solution:
    def maxSubArray(self, nums):
        max_so_far = nums[0] # make a initial value to ne zero
        max_ending_here = nums[0] # make ending value to be zero 
        for i in range(1, len(nums)): # take range from 1 to 11 
            max_ending_here = max(max_ending_here + nums[i], nums[i]) # max(-1,1) = 1 \ -2 , -3 = -2
            # Did we beat the 'maxSoFar' with the 'maxEndingHere'?
            max_so_far = max(max_ending_here, max_so_far) # max(1,-2) = 1 \

        return max_so_far
p = Solution()
result = p.maxSubArray([-2,1,-3,-4,9,-10,-11,-1,2,1,-5])        
print(result)