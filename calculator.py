import sys

def calculate(operand1, operand2, operation):
    if operation == '+':
        return operand1 + operand2
    elif operation == '-':
        return operand1 - operand2
    elif operation == 'MUL':
        return operand1 * operand2
    elif operation == '/':
        return operand1 / operand2
    else:
        raise ValueError("Invalid operation")

if __name__ == "__main__":
    operand1 = float(sys.argv[1])
    operand2 = float(sys.argv[2])
    operation = sys.argv[3]
    
    result = calculate(operand1, operand2, operation)
    print(f"Result: {operand1} {operation} {operand2} = {result}")
