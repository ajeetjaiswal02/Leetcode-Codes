#numberwithconsequative integer
class Solution:
    def numsSameConsecDiff(self, N, K):
        @lru_cache(None)
        def dfs(i,j):
            if j < 0 or j > 9 or (j == 0 and i == 1): return []
            if i == 1: return [str(j)]
            dirs, out = set([K, -K]), []
            for d in dirs:
                out += [s+str(j) for s in dfs(i-1,j+d)]
            return out
        
        if N == 1: return range(10)
        return list(chain(*[dfs(N, i) for i in range(10)]))

