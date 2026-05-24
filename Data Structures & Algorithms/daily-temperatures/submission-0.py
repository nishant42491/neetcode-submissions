class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        stack = list()

        output = [0 for i in range(len(temperatures))]

        for i,t in enumerate(temperatures):


            if len(stack) > 0:

                while  len(stack) > 0 and stack[-1][1] < temperatures[i]:

                    ind,temp = stack.pop()

                    output[ind] = i - ind 

            stack.append((i,t))

        return output



        
        