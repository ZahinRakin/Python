filename = "contains_number.txt"

with open(filename, "r") as f:
    numbers = f.read().split(', ')
    count = 0
    for number in numbers:
        if int(number) % 2 == 0:
            count += 1
print('number of even numbers in the file: ', count)