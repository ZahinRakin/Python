from pathlib import Path
from Card import show_tasks
import time


def create_account():
    print('Create an account?')
    want_acc = input('yes/no: ')
    if want_acc == 'yes':
        name = input('name: ')
        password = input('Password: ')
        with open(name+'.txt', "w") as f:
            f.write(password+'\n')
            print('An account has been created.')
        show_tasks(name)
    elif want_acc == 'no':
        print('fair enough.')
        print('exiting the app...')
        time.sleep(3)
        exit(0)
    else:
        print('You have chosen to do something ugly.')


def login():
    name = input("Name: ")
    password = input("Password: ")
    path = Path(name+'.txt')
    if path.exists():
        with open(path, "r") as f:
            f.seek(0)
            saved_pass = f.readline()
        if password == saved_pass:
            show_tasks(name)
        else:
            print('wrong password.')
            login()
    else:
        print(f"You don't have an account.\nYou are being redirected to the create account window.")
        create_account()
