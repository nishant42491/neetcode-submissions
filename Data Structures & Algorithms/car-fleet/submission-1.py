class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:


        sorted_arr = sorted(list(zip(position,speed)), key=lambda x:x[0])[::-1]

        times = [(target - sorted_arr[i][0])/sorted_arr[i][1] for i in range(len(sorted_arr))]

        stack =list()

        print(times)

        for t in times:

            if not stack or t > stack[-1]:
                stack.append(t)

        

        return len(stack)