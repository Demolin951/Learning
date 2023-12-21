import copy

def seaperate(list_of):
    list(list_of)
    list_of_example = copy.deepcopy(list_of)
    list_of_example.insert(-1,' and')
    if len(list_of_example) < 1:
        print('You need to write something')

    for o in range(len(list_of_example)):

        if o < len(list_of_example[0:-2]):
            print(str(list_of_example[o]),sep='',end=', ')
        else:
            print(str(list_of_example[o]),sep=' ',end=' ')

user_input = input()
user_input = user_input.split(' ')
seaperate(user_input)


