class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        import heapq
        neg_nums = [-x for x in nums]
        heapq.heapify(neg_nums)
        n = 0
        for _ in range(k):
            n = heapq.heappop(neg_nums)

        return -n