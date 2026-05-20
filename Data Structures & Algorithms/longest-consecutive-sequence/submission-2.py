class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        num_set = set(nums)

        out = 0

        for num in nums:

            m = 1

            out = max(out,m)

            cur = num

            while cur + 1 in num_set:

                m += 1

                out = max(out,m)

                cur += 1

        return out






        