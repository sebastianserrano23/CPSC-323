class Stack:
    def __init__(self):
        self.stack = []
    def push(self, item):
        self.stack.append(item)
    def pop(self):
        return self.stack.pop()
    def is_empty(self):
        return len(self.stack) == 0
def evaluate_postfix(expression, variables):
    stack = Stack()
    for char in expression:
        if char.isalpha():
            stack.push(variables[char])
        elif char in "+-*/^":
            operand2 = stack.pop()
            operand1 = stack.pop()
            if char == '+':
                stack.push(operand1 + operand2)
            elif char == '-':
                stack.push(operand1 - operand2)
            elif char == '*':
                stack.push(operand1 * operand2)
            elif char == '/':
                stack.push(operand1 / operand2)
            elif char == '^':
                stack.push(operand1 ** operand2)
    return stack.pop()
while True:
    variables = int(input("Enter the values of a, b, c and d: "))
    print(variables)
    expression = input("Enter a postfix expression with $ at the end: ")
    expression = expression.replace('$', '')
    print("Value =", evaluate_postfix(expression, variables))
    continue_choice = input("CONTINUE(y/n)? ")
    if continue_choice.lower() != 'y':
        break