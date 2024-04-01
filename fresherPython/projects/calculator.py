while True:
    print('What do you want to do?')
    print('1. Addition')
    print('2. Subtraction')
    print('3. Multiplication')
    print('4. Division')
    print('5. Modulo')
    print('6. Exponentiation')

    choice = input('Enter your choice: ')
    if choice == '1':
        num1 = float(input('Enter number 1: '))
        num2 = float(input('Enter number 2: '))
        print('Addition: ', num1 + num2)
    elif choice == '2':
        num1 = float(input('Enter number 1: '))
        num2 = float(input('Enter number 2: '))
        print('Subtraction: ', num1 - num2)
    elif choice == '3':
        num1 = float(input('Enter number 1: '))
        num2 = float(input('Enter number 2: '))
        print('Multiplication: ', num1 * num2)
    elif choice == '4':
        num1 = float(input('Enter dividend: '))
        num2 = float(input('Enter divisor: '))
        print('Quotient: ', num1 / num2)
    elif choice == '5':
        num1 = float(input('Enter dividend: '))
        num2 = float(input('Enter divisor: '))
        print('remainder: ', num1 % num2)
    elif choice == '6':
        num1 = float(input('Enter base: '))
        num2 = float(input('Enter exponent: '))
        print('Exponent: ', num1 ** num2)
    else:
        print('Invalid input')
