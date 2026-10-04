class Solution:
    def sortArrayByParityII(self, nums: list[int]) -> list[int]:
        L = 0
        R_even = len(nums) - 1
        R_odd = len(nums) - 1
        while L < min(R_even, R_odd):
            while L < min(R_even, R_odd) and ((L % 2 - nums[L] % 2) == 0):
                L += 1
            if L >= min(R_even, R_odd):
                break
            if nums[L] % 2 == 0:
                L_val = nums[L]
                while not (nums[R_odd] % 2 == 1 and R_odd % 2 == 0):
                    R_odd -= 1
                R_val = nums[R_odd]
                nums[L] = R_val
                nums[R_odd] = L_val
            elif nums[L] % 2 == 1:
                L_val = nums[L]
                while not (nums[R_even] % 2 == 0 and R_even % 2 == 1):
                    R_even -= 1
                R_val = nums[R_even]
                nums[L] = R_val
                nums[R_even] = L_val
        return nums
            