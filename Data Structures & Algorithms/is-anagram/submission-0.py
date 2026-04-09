class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s = sorted(s)
        t = sorted(t)
        count = 0
        if len(s) != len(t):
            return False
        while count < len(s):
            if s[count] != t[count]:
                return False
            count += 1
        return True
        