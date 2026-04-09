class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        return (len(set(nums)) != len(nums))
        nums.sort()
        count = 0
        while count < (len(nums) - 1):
            if nums[count] == nums[count + 1]:
                return True
            count +=1
        
        return False
        