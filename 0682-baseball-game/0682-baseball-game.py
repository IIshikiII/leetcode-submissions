class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for operation in operations:
            if operation.isdigit() or (len(operation) > 0 and operation[1:].isdigit()):
                stack.append(int(operation))
            elif operation == "C":
                stack.pop()
            elif operation == "D":
                stack.append(stack[-1] * 2)
            elif operation == "+":
                stack.append(stack[-1] + stack[-2])
        
        return sum(stack)