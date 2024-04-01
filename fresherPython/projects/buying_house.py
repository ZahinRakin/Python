credit_state = input("What is your credit(good or bad): ")
if credit_state.lower() == 'good':
    print('Down payment for house: ', 1000000*(10/100))
else:
    print('Down payment for house: ', 1000000*(20/100))
