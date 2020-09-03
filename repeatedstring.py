# to check if the element in the string are repeated or not
class solution():
    def reteatedstring(self,s): #abab
        for i in range(1,len(s)//2+1):
            if s[:i] * (len(s)//i)==s:
                return True
        return False

p = solution()
print(p.reteatedstring("abab"))
print("Time Complexity is O(1) and space complexity is O(mn)")
print("m: length  of repeated string")
print("n: length of element")
print("All codes is written by Ajeet want to contribute and increase the efficency  feel free to fork and push into the repository")