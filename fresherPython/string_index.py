course = 'python for beginners'
print(course[0])
print(course[-1])  # this is weird
print(course[2:5])  # this won't include the char at index 5
print(course[:5])
print(course[4:])
print(course[1:-1])

name = 'rakin'
name2 = name
print(name2)
name3 = name[:]
print(name3)

first = 'zahin'
last = 'rakin'
message = first + '[' + last + ']' + ' is a coder'
message2 = f''
print(message)
