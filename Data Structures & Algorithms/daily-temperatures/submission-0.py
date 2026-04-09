class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        out = []

        for i in range(len(temperatures)):
            for j in range(i + 1, len(temperatures)):

                if temperatures[i] < temperatures[j]:
                    out.append(j-i)
                    break
                elif (temperatures[i] >= temperatures[j]) and j != (len(temperatures) -1):
                    continue
                else:
                    out.append(0)
        
        out.append(0)
                
        return out


        