def collatz(number):
    if number % 2:
        return 3 * number + 1
    else:
        return number // 2

while True:
    number = input("Enter a number: ")
    try:
        number = int(number)
        break
    except ValueError:
        print("The value entered must be an integer.")


while number != 1:
        number = collatz(number)
        print(number)
