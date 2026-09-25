class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        depth = 0
        res_str = ""
        for char in s:
            if depth == 1 and char == "(":
                res_str =  res_str + char
            elif depth == 1 and char == ")":
                depth = 0
                continue
            elif depth >= 2:
                res_str =  res_str + char

            if char == "(":
                depth += 1
            elif char == ")":
                depth -= 1
        return res_str
            

