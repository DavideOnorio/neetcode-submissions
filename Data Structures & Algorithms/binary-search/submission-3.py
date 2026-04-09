class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0, len(nums)-1
        
        while l <= r:
            guess = ((r + l) // 2)

            if nums[guess] == target:
                return guess
            elif nums[guess] > target:
                r = guess-1
            else:
                l = guess+1
        
        return -1