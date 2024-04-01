dimension = [7, 7, 2, 2, 5, 5, 2, 2, 2]
count = 0
for i in dimension:
    for j in range(i):
        print(f'{count % 10} ', end='')
        count += 1
    print()
