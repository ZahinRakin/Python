while True:
    dec_to_str = {
        0: 'zero',
        1: 'one',
        2: 'two',
        3: 'three',
        4: 'four',
        5: 'five',
        6: 'six',
        7: 'seven',
        8: 'eight',
        9: 'nine'
    }

    take_in = input('Enter number: ')
    for char in take_in:
        print(dec_to_str.get(int(char)), end=' ')
    print()
