class Solution:
    def minOperations(self, logs: list[str]) -> int:
        stack = []
        for log in logs:
            if log == "./" or (not stack and log == "../"):
                continue
            elif stack and log == "../":
                stack.pop(-1)
            else:
                stack.append(log)
        return len(stack)
        