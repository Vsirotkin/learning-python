catNames = []
while True:
    name = input(f'Enter the name of cat or enter nothing to stop.): ')
    if name == '':
        break
    else:
        catNames.append(name)  # list concatenation
print('The cat names are: ')
for i in range(len(catNames)):
    print(f'{i + 1}. - {catNames[i]}')
