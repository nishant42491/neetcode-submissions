import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        low = 1
        high = max(piles)

        def calculate_hours(eat_rate):

            out  = sum([math.ceil(i/eat_rate) for i in piles])

            return out

        r = None

        while low <= high:

            mid = (low + high)//2

            print("low:", low)
            print("high:", high)
            print("mid:", mid)

            time_taken = calculate_hours(mid)

            if time_taken > h:

                low = mid + 1

            else:

                high = mid - 1
                r = mid


        return r





        