# how to use lambda


def add1(one, two):
    return one + two


add2 = lambda one, two: one + two

print(add1(2, 8))
print(add2(2, 6))

more_then_one_nums = filter(lambda x: x > 1, [1, 2, 3, 8, 56])
print(list(more_then_one_nums))
