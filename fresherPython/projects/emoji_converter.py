emotions = {
    ':)': 'happy',
    ';)': 'winkle',
    ':(': 'sad'
}

message = input('> ')
for string in message.split(' '):
    if emotions.get(string) is not None:
        print(emotions.get(string), end=' ')
    else:
        print(string, end=' ')
