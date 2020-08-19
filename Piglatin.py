# This Question is asked by uber for sde Role
#Pig Latin
# If string contain aeiou add ma to end
# if constrant remove frist element and add to the end with ma
# add a for every element

class Solution():
    def toGoatLatin(self,S):
        temp = S.split(" ")
        counter = 1
        result = []
        vowels = ("a","e","i","o","u")
        for i in temp:
            if i[0].lower() in vowels:
                x = i + "ma" + ('a'*counter)
            else:
                x = i[1:] + i[0] + "ma" + ('a'*counter)
            counter += 1
            result.append(x)
        return " ".join(c for c in result) 
p = Solution()
result = p.toGoatLatin("oello my name is Ajeet")
print(result)           



