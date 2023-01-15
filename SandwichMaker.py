import pyinputplus as pyip
breadTypes = {'wheat': 15, 'white': 10, 'sourdough': 20}
proteinTypes = {'chicken': 7, 'turkey': 10, 'ham': 15, 'tofu': 7}
cheeseTypes = {'cheddar': 5, 'swiss': 10, 'mozzarella': 5}
condimentTypes = ['mayo', 'mustard', 'lettuce', 'tomato']
discount = {1500: 25, 1000: 10, 700: 5, 200: 2}
price = 0

bread = pyip.inputMenu(list(breadTypes.keys()), prompt = 'Choose a bread type: \n')
price += breadTypes[bread]

protein = pyip.inputMenu(list(proteinTypes.keys()), prompt = 'Choose a protein type: \n')
price += proteinTypes[protein]

cheeseornot = pyip.inputYesNo(prompt = 'Would you like some cheese? ')
if cheeseornot.lower()[0] == 'y':
    cheese = pyip.inputMenu(list(cheeseTypes.keys()), prompt = 'What kind of cheese would you like? \n')
    price += cheeseTypes[cheese]

condiment = []
for i in condimentTypes:
    choice = pyip.inputYesNo(prompt = 'Would you like any %s? ' % i)
    condiment.append(choice)

count = pyip.inputInt(prompt = 'How many sandwiches would you like? ', min = 1)
price *= count

for i in list(discount.keys()):
    if price >= i:
        print(discount[i])
        price -= discount[i]*price/100
        break

print('The total bill amounts to Rs.', price)