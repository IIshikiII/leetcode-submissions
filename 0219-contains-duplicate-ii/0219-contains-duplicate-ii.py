class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        if len(nums) <= 1:
            return False
        
        start_set = set(nums[0:k+1])
        if len(start_set) < min(len(nums), k + 1):
            return True
        
        for i in range(len(nums)-k-1):
            start_set.remove(nums[i])
            start_set.add(nums[i+k+1])

            if len(start_set) < k + 1:
                return True
        
        return False