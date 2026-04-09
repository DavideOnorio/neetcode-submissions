class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        op = {'+': lambda x, y: x + y, '-': lambda x, y: x - y, '*': lambda x, y: x * y, '/': lambda x, y: int(x / y)}
        for i,t in enumerate(tokens):

            if t in op.keys():
                y = int(stack.pop())
                x = int(stack.pop())
                res = op[t](x, y)
                stack.append(res)
            else:
                stack.append(tokens[i])

        return int(stack[0])