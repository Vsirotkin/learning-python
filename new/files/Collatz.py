# Write a function named collatz() that has one parameter named number. If number is even,
# then collatz() should print number // 2 and return this value. If number is odd,
# then collatz() should print and return 3 * number + 1.
import sys

def collatz(number) -> object:
    if number % 2 == 0:
        return print(number // 2)
    else:
        return print(3 * number + 1)

while True:
    try:
        user_number = int(input('enter a number: '))
        if user_number != 1:
            collatz(user_number)
            continue
        else:
            print('good bye!')
            sys.exit()
    except ValueError:
        print('only integer!!!')
