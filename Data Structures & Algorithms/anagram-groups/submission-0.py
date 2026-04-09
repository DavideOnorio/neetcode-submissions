class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        out = []
        strs = sorted(strs)
        dicte = {}
        

        if len(strs) == 1:
            out.append(strs)
            return out

        for word in strs:
            key = tuple(sorted(word))
            if key in dicte:
                dicte[key].append(word)
            else:
                dicte[key] = [word]

        return list(dicte.values())
                    
                



        