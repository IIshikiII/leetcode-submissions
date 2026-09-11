class Solution:
    def reverseWords(self, s: str) -> str:
        stack = []
        res_str = ""
        for char in s:
            if char != " ":
                stack.append(char)
            else:
                while stack:
                    stack_top_char = stack.pop()
                    res_str += stack_top_char
                res_str += char
        while stack:
            stack_top_char = stack.pop()
            res_str += stack_top_char    
        return res_str
        