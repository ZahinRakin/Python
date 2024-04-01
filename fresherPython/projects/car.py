import time

running = False

while True:
    prompt = input()
    if prompt.lower() == 'help':
        print('''Available commands:
        \tstart.
        \tstop.
        \tquit.''')
    elif prompt.lower() == 'start':
        if not running:
            print('car has been started and it is running now...')
            running = True
        else:
            print('WTF bro. What are you doing?...')
    elif prompt.lower() == 'stop':
        if running:
            print('Car has been stopped.')
            running = False
        else:
            print('WTF bro. What are you doing?')
    elif prompt.lower() == 'quit':
        print('Bye bye!')
        time.sleep(1)
        break
    else:
        print('invalid command.')
