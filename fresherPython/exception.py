while True:
    try:
        dividend = float(input('Enter the dividend: '))
        divisor = float(input('Enter the divisor: '))
        print('Quotient: ', dividend/divisor)
    except ZeroDivisionError as e:
        print('Error: ', e)
    finally:
        print('this will be executed regardless of encountering the error...')
