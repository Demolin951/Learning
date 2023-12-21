import sys
def collatz(number):
    try:
        number = str.lower(number)
        if number == 'exit':
            sys.exit()

        number = int(number)
        if number % 2 == 0:
            number = number // 2
            print(str(number))
        elif number % 2 == 1:
            number = 3 * number + 1
            print(str(number))
    except ValueError:
        print('You must write only integers.')

print('This is calculator of Kollatz sequence. Write any number to start. Type exit to quit.')
while True:
    collatz(input())
