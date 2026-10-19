class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:

        for i in range(0,len(nums)):
            
            if i == 0:
                continue
            
            else:
                nums[i] = nums[i] + nums[i-1]

        return nums
        