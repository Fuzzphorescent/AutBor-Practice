import random
numberOfStreakingLists = 0
for experimentNumber in range(10000):
    # Code that creates a list of 100 'heads' or 'tails' values.
    L = []
    for i in range(100):
        L.append(random.randint(0,1))

    # Code that checks if there is a streak of 6 heads or tails in a row.
    for i in range(95):
        if L[i:i+6] == [0,0,0,0,0,0] or L[i:i+6] == [1,1,1,1,1,1]:
            numberOfStreakingLists += 1
            break
print('Chance of streak: %s%%' % (numberOfStreakingLists / 100))