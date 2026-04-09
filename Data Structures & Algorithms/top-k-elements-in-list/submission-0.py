class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dicte = {}

        for num in nums:
            if num in dicte:
                dicte[num] += 1
            else: 
                dicte[num] = 1

        return sorted(dicte.keys(), key=lambda x: dicte[x])[-k:]
