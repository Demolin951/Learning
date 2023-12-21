import random
def count_consecutive_numbers(lst):
    count = 0
    count1 = 0
    for i in range(1,len(lst)):
        if lst[i] == lst[i - 1]:
            count += 1
        else:
            count = 0
        if count == 5:
            count1 += 1
    return count1

numberOfTries = 0
numberOfStreaks = 0
coin_flip_list = []
for experimentNumber in range(10000):
    if len(coin_flip_list) < 99:
        coin_flip = random.randint(0, 1)
        coin_flip_list.append(coin_flip)
    else:
        numberOfStreaks = numberOfStreaks + count_consecutive_numbers(coin_flip_list)
        numberOfTries += 1
        coin_flip_list = []

print('Chance of streak: %s%%' % (numberOfStreaks / 10000))
