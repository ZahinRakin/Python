import time
from to_do.User import login, create_account


print('Welcome to to_do app!')
print('Do you have an account?')
has_acc = input('yes/no: ')
if has_acc == 'yes':
    login()
elif has_acc == 'no':
    create_account()
