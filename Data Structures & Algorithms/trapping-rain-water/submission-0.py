class Solution:
    def trap(self, height: List[int]) -> int:

        prefix = []
        suffix = []

        p = 0
        s = 0

        for i in height:

            prefix.append(p)

            p = max(p,i)

        rev = height[::-1]

        for i in height[::-1]:

            suffix.append(s)

            s = max(s,i)

        suffix = suffix[::-1]

        ar = 0

        for i in range(len(height)):

            water = max(min(prefix[i], suffix[i]) - height[i],0)

            ar += water

        print(prefix)
        print(suffix)
        return ar


        