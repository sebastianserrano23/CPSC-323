def evaluate_postfix(expression):
    stack = []
    # Split the expression into tokens
    for token in expression.split():
        # If the token is a digit, push it onto the stack
        if token.isdigit():
            stack.append(int(token))
        # If the token is a variable name (consisting of alphabetic characters), prompt the user to enter its value
        elif token.isalpha():
            value = int(input(f"Enter the value of {token}: "))
            stack.append(value)
        # If the token is an operator, pop the operands from the stack, perform the operation, and push the result back onto the stack
        else:
            operand2 = stack.pop()
            operand1 = stack.pop()
            if token == '+':
                stack.append(operand1 + operand2)
            elif token == '-':
                stack.append(operand1 - operand2)
            elif token == '*':
                stack.append(operand1 * operand2)
            elif token == '/':
                stack.append(operand1 / operand2)
    # The final result is at the top of the stack
    return stack[0]

def main():
    while True:
        # Prompt the user to enter a postfix expression
        expression = input("Enter a postfix expression with a $ at the end: ")
        # Check if the expression ends with '$'
        if expression[-1] != '$':
            print("Invalid expression format. Expression must end with a $.")
            continue
        
        # Evaluate the expression and print the result
        result = evaluate_postfix(expression[:-1])  # Exclude the '$' symbol from the expression
        print("Expression's value is", result)
        
        # Ask the user if they want to continue
        choice = input("CONTINUE (y/n)? ")
        if choice.lower() != 'y':
            break

if __name__ == "__main__":
    main()