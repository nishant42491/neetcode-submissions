class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        two_sum_dict = {}

        for i,n in enumerate(numbers):

            if n in two_sum_dict:

                return [two_sum_dict[n]+1, i+1]

            two_sum_dict[target-n] = i

        return None




        