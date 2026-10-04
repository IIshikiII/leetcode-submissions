class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        stack = []

        for ast in asteroids:
            if (not stack) or (stack[-1] < 0) or (ast > 0):
                stack.append(ast)
            else:
                while stack and (abs(ast) > abs(stack[-1])) and stack[-1] > 0:
                    stack.pop(-1)
                if stack and stack[-1] < 0:
                    stack.append(ast)
                elif stack and (abs(ast) == abs(stack[-1])):
                    stack.pop(-1)
                    continue
                elif stack and (abs(ast) < abs(stack[-1])):
                    continue
                elif not stack:
                    stack.append(ast)

        return stack


        