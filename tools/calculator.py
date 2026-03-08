def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ValueError("Cannot divide by zero")
    return x / y

def power(x, y):
    return x ** y

def modulo(x, y):
    if y == 0:
        raise ValueError("Cannot perform modulo by zero")
    return x % y
def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")
            
def main():
    print('This is the first CLI tool in my Python CLI tools repository!')
    print('Welcome to the calculator!')
    print('Please select an operation:')
    print('1. Add')
    print('2. Subtract')
    print('3. Multiply')
    print('4. Divide')
    print('5. Power')
    print('6. Modulo')
    

    while True:
        try:
            operation_choice = int(input('Enter the number corresponding to the desired operation (1/2/3/4/5/6), enter 0 to exit: '))
        except ValueError:
            print('Invalid input. Please enter a number.')
            continue
        if operation_choice not in [0, 1, 2, 3, 4, 5, 6]:
            print('Invalid choice. Please select a valid operation.')
            continue
        if operation_choice in [1, 2, 3, 4, 5, 6]:
            print('Please enter two numbers:')
            x = get_number('Enter the first number: ')
            y = get_number('Enter the second number: ')
        if operation_choice == 1:
            print(add(x, y))
        elif operation_choice == 2:
            print(subtract(x, y))
        elif operation_choice == 3:
            print(multiply(x, y))
        elif operation_choice == 4:
            print(divide(x, y))
        elif operation_choice == 5:
            print(power(x, y))
        elif operation_choice == 6:
            print(modulo(x, y))
        elif operation_choice == 0:
            print('Thank you for using the calculator!')
            break
    
        
    

if __name__ == "__main__":
    main()