#car pooling question asked in VArious commapnies
# GOOGLE , AMAZON , UBER , Microsoft

class Solution:
    def carPooling(self, trips,capacity):
        timestamp = [0] * 1001
        for trip in trips:
            timestamp[trip[1]] += trip[0]
            timestamp[trip[2]] -= trip[0]

        used_capacity = 0
        for passenger_change in timestamp:
            used_capacity += passenger_change
            if used_capacity > capacity:
                return False

        return True
p = Solution()
result = p.carPooling(trips=[[2,1,5],[3,3,7]],capacity=6)        
print(result)