class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        out = []
        count = 0

        while count < len(nums):
            removed_item = nums.pop(count)
            prod = 1
            for j in nums:
                prod *= j
            out.append(prod)
            nums.insert(count, removed_item)
            count +=1
        
        return out

        