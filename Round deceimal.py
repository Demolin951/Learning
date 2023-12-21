# Write your code here :-)
def get_rounded_number(number_str):
    return str(round(float(number_str),2))

print('Write any number and i will round it up to deceimal.Type exit whenever you want')

while True:
    user_input=input()

    if user_input.lower()=='exit':
     break

    try:

        print('Here is your number: ' + get_rounded_number(user_input))


    except ValueError:

        print('You must write only numbers')







