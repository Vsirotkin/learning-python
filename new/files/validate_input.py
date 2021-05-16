# to check whether an input has the demanded values

while True:
    age = input('what is your age? ')
    if age.isdecimal():
        break
    else:
        print('only numbers')

while True:
    password = input('enter a password: ')
    if password.isalnum():
        print('welcome!')
        break
    else:
        print('only characters or numbers')
