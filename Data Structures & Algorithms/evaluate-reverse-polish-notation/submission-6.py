class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []
        curRes = 0
        operators = ["+", "-", "*", "/"]
        
        for token in tokens:
            if token in operators:
                if stack:
                    operand1 = int(stack.pop())
                    operand2 = int(stack.pop())
                    if token == "+":
                        res = operand1 + operand2
                    if token == "-":
                        res = operand2 - operand1
                    if token == "/":
                        res = operand2 / operand1
                    if token == "*":
                        res = operand1 * operand2
                    stack.append(res)
            else:
                stack.append(token)
        return int(stack[0])