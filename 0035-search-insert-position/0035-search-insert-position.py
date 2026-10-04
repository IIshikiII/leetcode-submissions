class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        if nums[-1] < target:
            return len(nums)
        elif nums[0] >= target:
            return 0
        
        L = 0
        R = len(nums) - 1
        while L < R - 1:
            mid = (L + R) // 2
            mid_val = nums[mid]
            if mid_val == target:
                return mid
            elif mid_val < target:
                L = mid
            elif mid_val > target:
                R = mid
        
        return L + 1
