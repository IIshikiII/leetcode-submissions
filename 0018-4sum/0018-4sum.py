class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[list[int]]:
        nums.sort()
        
        res = []
        L = 0
        R = len(nums) - 1
        while L < R:
            if nums[L] + nums[R] == target:
                if [nums[L], nums[R]] not in res:
                    res.append([nums[L], nums[R]])
                L += 1
            elif nums[L] + nums[R] < target:
                L += 1
            elif nums[L] + nums[R] > target:
                R -= 1

        # print("twoSum", nums, target, res)
        return res
    
    def threeSum(self, nums: list[int], target: int) -> list[list[int]]:
        nums.sort()
        # print("threeSum", nums)
        res = []
        for i in range(len(nums)-2):
            for lst in self.twoSum(nums[i+1:], target-nums[i]):
                if [nums[i]] + lst not in res:
                    res.append([nums[i]] + lst)
        return res

    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        nums.sort()
        res = []
        for i in range(len(nums)-3):
            for lst in self.threeSum(nums[i+1:], target-nums[i]):
                if [nums[i]] + lst not in res:
                    res.append([nums[i]] + lst)
        return res

