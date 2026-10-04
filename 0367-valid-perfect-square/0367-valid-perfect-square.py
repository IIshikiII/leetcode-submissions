class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num == 1:
            return True
        min_val = 1
        max_val = num // 2
        while min_val <= max_val:
            mid = (min_val + max_val) // 2
            if mid * mid == num:
                return True
            elif mid * mid < num:
                min_val = mid + 1
            else:
                max_val = mid - 1
            
        return False