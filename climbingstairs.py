class Solution():
    def climbing(self,num):
        memo = {}
        if num == 1 or num == 0:
            return 1
        memo[num] = [None] * (num + 1)
        memo[1] = 1
        memo[2] = 2
        for i in range(3,num+1):
            memo[i] = memo[i-1] + memo[i-2]
        return memo[num]
p = Solution()
result = p.climbing(5)
print(result)            
