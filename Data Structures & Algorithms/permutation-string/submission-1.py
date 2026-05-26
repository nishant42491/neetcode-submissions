class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s2) < len(s1):
            return False

        count_map = [0 for i in range(26)]


        for ch in s1:

            ind = ord(ch) - 97
            count_map[ind] += 1

        
        size = len(s1)

        print(count_map)

        for i in range(size):

            ch = s2[i]

            count_map[ord(ch) - 97] -= 1

        if all(c == 0 for c in count_map):
            return True

        l = 0

        r = size - 1

        while r < len(s2):

            print(count_map)

            
            lchar = s2[l]

            count_map[ord(lchar) - 97] += 1
            l += 1

            r+=1

            if r == len(s2):
                break
            rchar = s2[r]
            count_map[ord(rchar) - 97] -= 1

            if all(c == 0 for c in count_map):
                return True

        
        return False









            

        






        


        


        
        