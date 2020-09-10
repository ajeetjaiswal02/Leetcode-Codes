from collections import defaultdict
class solution():
    def gethint(self,secret,guess):
        bulls,cows = 0,0
        counter = defaultdict(int)

        for idx in range(len(secret)):
            s= secret[idx]
            g = guess[idx]
            
            if s==g:
                bulls += 1
            else:
                if counter[s]<0:
                    cows +=1
                if counter[g]>0:
                    cows +=1
                counter[s] +=1
                counter[g] -=1
        return  f"{bulls}A{cows}B"

p= solution()
result = p.gethint('1232','1239')
print(result)
        