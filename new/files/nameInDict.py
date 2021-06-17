# new way to get val for indicated key

fruits = [
    {'name': 'apple'},
    {'name': 'avocado'},
    {'name': 'banana'}
]

print([fruit['name'] for fruit in fruits if 'a' == fruit['name'][-1]])
