class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if len(s) == 0:

            return 0

        if len(s) == 1:

            return 1
        
        l = 0
        r = 0

        in_string = set()
        in_string.add(s[l])
        count = 0

        while r < len(s):
            
            r += 1

            if r == len(s):
                break

            while  r < len(s) and(s[r] in in_string) == True:
                c = s[l]

                in_string.remove(c)

                l = l + 1
            
            in_string.add(s[r])

            count = max(count, r-l)

        return count + 1





        