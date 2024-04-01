def show_tasks(name: str):
    with open(name + '.txt', "r") as f:
        data = f.readlines()
    task_count = len(data)-1
    print('Tasks: ')
    for line in data:
        print(line, end='')
    print('\n')
    print('What would you like to do?\n')
    print('a. add a task.')
    print('b. mark as done.')
    print('c. mark as undone.')
    print('d. delete a task.\n')

    choice = input('choose : ')
    if choice == 'a':
        task = input('Enter the task: ')
        task_count += 1
        data.append(f'{task_count}. {task}.\n')
    elif choice == 'b':
        done_job = input('Which job you completed? : ')
        data[int(done_job)] = f'{done_job}. done'
    elif choice == 'c':
        undone_job = input('Which job you missed to complete? : ')
        data[int(undone_job)] = f'{data[int(undone_job)]} undone'
    elif choice == 'd':
        del_job = input('Which job you wanna delete? : ')
        data[int(del_job)] = ' '
    with open(name+'.txt', "w") as f:
        for line in data:
            f.write(line)
    show_tasks(name)