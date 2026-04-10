class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        while len(stones) > 1:
            y_index = stones.index(max(stones))
            y = stones.pop(y_index)
            x_index = stones.index(max(stones))
            x = stones.pop(x_index)

            if x == y:
                continue
            if x < y:
                stones.append(y-x)
                
        if len(stones) == 0:
            return 0
        else: 
            return stones[0]
            
