class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        for i in matrix:
            if i[0] <= target and i[-1] >= target:
                l,r = 0, len(i) - 1
                while l <= r:
                    guess = (l+r)//2

                    if i[guess] == target:
                        return True
                    elif i[guess] <= target:
                        l = guess + 1
                    else:
                        r = guess - 1
                
        return False
        


