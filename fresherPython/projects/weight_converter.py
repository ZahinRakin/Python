while True:
    weight = float(input('Enter weight = '))
    lb_or_kg = input('Enter lb or kg = ')

    if lb_or_kg.lower() == 'lb':
        print(f'{weight}lb is equal to {weight * .45} kg.')
    elif lb_or_kg.lower() == 'kg':
        print(f'{weight}kg is equal to {weight * 2.205} lb.')
    else:
        print('Invalid weight.')
