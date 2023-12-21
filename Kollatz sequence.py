def collatz(number):
    try:
        number = int(number)
        if number % 2 == 0:
            number = number // 2
            print(str(number))
        elif number % 2 == 1:
            number = 3 * number + 1
            print(str(number))
        return str(number)
    except ValueError:
        print('You must write only integers.')
        return None

print('This is calculator of Kollatz sequence. Write any number to start. Type exit to quit.')
while True:
    statement = collatz(input())
    if statement.lower() == 'exit':
        break
    else:
        collatz(input(statement))
