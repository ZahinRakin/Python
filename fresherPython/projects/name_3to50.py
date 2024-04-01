name = input("Wnter your name: ")
if len(name) <= 3:
    print("name's length should be higher than 3.")
elif len(name) >= 50:
    print("name's length should less than to 50.")
else:
    print('name looks fine.')
