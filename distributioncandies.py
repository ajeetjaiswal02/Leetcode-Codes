#[1,2,3,0] candies = 6 num_of_people = 4 
class Solution():
    def distribution(self,candies,num_of_people):
        array = [0] * num_of_people
        index = 0
        while candies > 0:
            array[index%num_of_people] += min(num_of_people,index+1)
            candies-= (index+1)
            index+=1
        return array
p = Solution()
result = p.distribution(145,8)
print(result)            
