class Calculator:
    def add(self, a, b):
        return a + b
    
    def subtract(self, a, b):
        return a - b
    
    def multiply(self, a, b):
        return a * b
    
    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b

def main():
    calc = Calculator()
    print("Calculator")
    print("Operations: +, -, *, /")
    
    try:
        num1 = float(input("Enter first number: "))
        operator = input("Enter operator: ")
        num2 = float(input("Enter second number: "))
        
        if operator == '+':
            result = calc.add(num1, num2)
        elif operator == '-':
            result = calc.subtract(num1, num2)
        elif operator == '*':
            result = calc.multiply(num1, num2)
        elif operator == '/':
            result = calc.divide(num1, num2)
        else:
            print("Invalid operator")
            return
        
        print(f"Result: {result}")
    
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    main()
