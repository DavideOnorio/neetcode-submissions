class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        import math
        dist = {}
        out = []
        while points:
            p = points.pop()
            x,y = p
            d = math.sqrt((x - 0)**2 + (y - 0)**2)
            dist[tuple(p)] = d
        
        lowest = sorted(dist.items(), key=lambda x: x[1])[0:k]
        
        for point, value in lowest:
            out.append(list(point))
        
        return out

