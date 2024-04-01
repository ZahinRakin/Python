filename = "practice.txt"
word = "learning"

with open(filename, "w") as f:
    message = '''Hi everyone
we are learning File I/O
using java
I like programming in java.'''
    f.write(message)

with open(filename, "r+") as f:
    data = f.read()
    print("data before: ", data)
    new_data = data.replace("java", "Python")
    f.seek(0)
    f.write(new_data)
with open(filename, "r") as f:
    data = f.read()
    print("data after: ", data)
    if data.find(word) != -1:
        print("found.\n")
    else:
        print("not found.\n")
