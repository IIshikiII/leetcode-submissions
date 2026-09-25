class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        res_list = []
        L = 0
        R = len(nums) - 1
        while L <= R:
            L_val = nums[L]
            R_val = nums[R]
            if abs(L_val) >= abs(R_val):
                res_list.append(L_val * L_val)
                L += 1
            else:
                res_list.append(R_val * R_val)
                R -= 1
        return res_list[::-1]