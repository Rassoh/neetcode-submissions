class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ## go through each value
        ## create a stack of passed/seen days 
        ## when you find a day with a higher temperature you return the length of the stack and reset it, moving on to the next day
        res = [0] * len(temperatures)
        stack = []

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackT, stackInd = stack.pop()
                res[stackInd] = (i - stackInd)
            stack.append([t,i])
        return res