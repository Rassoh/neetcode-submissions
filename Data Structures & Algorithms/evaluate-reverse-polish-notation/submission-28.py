class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ##create stack 
        ##last in first out 
        ##numbers get added to stack
        ##Operand then pops the last 2 numbers and performs operation
        ##e.g [3,4] followed by '-' = 
        ## minus pops 3 then '-' then pops 4 
        ## 3 - 4 = -1 
        ##the answer -1 is then added back into the stack 
        ans = 0 
        stack = []
        operands = ['-','+','*','/']
        for token in tokens:
            if token in operands:
                int1 = stack.pop()
                int2 = stack.pop()
                if token == "+":
                    ans = int(int2) + int(int1)
                if token == "-":
                    ans = int(int2) - int(int1)
                if token == "*":
                    ans = int(int2) * int(int1)
                if token == "/":
                    ans = int(int2) / int(int1)
                stack.append(int(ans))
            else:
                stack.append(token)
        return int(stack[0])
            