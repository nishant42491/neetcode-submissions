class Solution:
    def maxArea(self, heights: List[int]) -> int:

        l = 0
        r = len(heights)-1

        out = 0

        while l < r:

            ar = min(heights[l], heights[r])

            distance = r-l

            out = max(out, ar*distance)

            if heights[l] < heights[r]:

                l += 1

            else:
                r -= 1

        
        return out

