class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        parent = {')' : '(', '}' : '{', ']': '['}
        for i in range(len(s)):
            stack.append(s[i])
            if len(stack) == 1:
                continue
            if stack[-1] in parent.values():
                continue
            elif parent[stack[-1]] == stack[-2]:
                stack.pop()
                stack.pop()
        return True if len(stack) == 0 else False


        