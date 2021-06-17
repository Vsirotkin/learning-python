# new way to get val for indicated key

fruits = [
    {'name': 'apple', 'price': 20},
    {'name': 'avocado', 'price': 10},
    {'name': 'banana', 'price': 5}
]

print([fruit['name'] for fruit in fruits if 'a' == fruit['name'][-1]])
print(
    {fruit['name']: fruit['price'] for fruit in fruits}
)
