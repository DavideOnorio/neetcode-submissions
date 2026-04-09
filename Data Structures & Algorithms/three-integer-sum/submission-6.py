class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        out = []

        for i in range(len(nums)):
            l,r = 0, len(nums)-1
            while l < r:
                if l == i:
                    l += 1
                    continue
                elif r == i:
                    r -= 1
                    continue

                if (nums[l] + nums[i]) == -nums[r]:
                    if sorted([nums[l], nums[i], nums[r]]) in out:
                        l += 1
                        continue
                    out.append(sorted([nums[l], nums[i], nums[r]]))
                    l += 1
                    
                elif (nums[l] + nums[i]) < -nums[r]:
                    l += 1
                elif (nums[l] + nums[i]) > -nums[r]:
                    r -= 1
        
        return out