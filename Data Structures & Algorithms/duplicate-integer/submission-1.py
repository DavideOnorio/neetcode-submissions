class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        count = 0
        while count < (len(nums) - 1):
            if nums[count] == nums[count + 1]:
                return True
            count +=1
        
        return False
        