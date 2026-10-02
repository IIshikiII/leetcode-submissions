class Solution:
    def sortArrayByParity(self, nums: list[int]) -> list[int]:
        L = 0
        R = len(nums) - 1
        while L < R:
            while nums[L] % 2 == 0 and L < R:
                L += 1
            while nums[R] % 2 == 1 and L < R:
                R -= 1
            if nums[L] % 2 == 1 and nums[R] % 2 == 0:
                l_val = nums[L]
                r_val = nums[R]
                nums[L] = r_val
                nums[R] = l_val
        return nums
