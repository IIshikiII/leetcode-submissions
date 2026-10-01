class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        for i, char in enumerate(s):
            if not stack:
                stack.append(char)
                continue
            elif char.isupper():
                if stack[-1].islower() and (char.lower() == stack[-1]):
                    stack.pop(-1)
                    continue
            elif char.islower():
                if stack[-1].isupper() and (char.upper() == stack[-1]):
                    stack.pop(-1)
                    continue
            stack.append(char)

        return "".join(stack)