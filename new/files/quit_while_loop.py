# conditions
import sys

spam = input('enter any figure: ')

while True:
    if spam == 'q':
        print('See you.')
        sys.exit()
    elif spam == '1' or spam == '2' or spam == '3':
        continue
    else:
        spam = input('any figure: ')

if spam == '1':
    print('Leo')
elif spam == '2':
    print('Kate')
else:
    print('Nothing')
