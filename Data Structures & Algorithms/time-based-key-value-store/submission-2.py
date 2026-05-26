from collections import defaultdict

class TimeMap:

    def __init__(self):

        self.map = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:

        self.map[key].append((value,timestamp))

    def get(self, key: str, timestamp: int) -> str:


        items = self.map[key]

        t = timestamp

        low = 0

        high = len(items) - 1


        output = ""

        while low <= high:

            mid = (low + high)//2


            if items[mid][1] == t:

                return items[mid][0]

            elif items[mid][1] > t:

                high = mid - 1

            else:
                low = mid + 1
                output = items[mid][0]


        return output


        
