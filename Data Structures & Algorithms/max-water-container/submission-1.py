class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l,r = 0, len(heights)-1
        past_max = 0
        while l < r:
            
            if (min(heights[l], heights[r])* (r-l)) > past_max:
                past_max = (min(heights[l], heights[r])* (r-l))
            
            if heights[l] > heights[r]:
                r -= 1
                continue
            elif heights[l] <= heights[r]:
                l += 1
                continue
            
        return past_max


        