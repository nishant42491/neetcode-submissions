class Solution:
    def isValid(self, s: str) -> bool:

        stack = list()

        mapp = {"}": "{", "]":"[", ")":"("}

        for b in s:

            if b == "(" or b == "{" or b == "[":

                stack.append(b)

            else:

                out = mapp[b]

                if len(stack) == 0 or stack.pop() != out:

                    return False


        return True if len(stack) == 0 else False
            
        