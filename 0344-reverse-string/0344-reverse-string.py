class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        L = 0
        R = len(s) - 1
        while L <= R:
            l_val = s[L]
            r_val = s[R]
            s[L] = r_val
            s[R] = l_val
            L += 1
            R -= 1