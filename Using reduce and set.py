from functools import reduce

tup_list = [(15, 3), (3, 9), (1, 10), (99, 2)]

digit_list = set(reduce(lambda a,b: str(a) + str(b), tup) for tup in tup_list)
digit_list = set(digit for string in digit_list for digit in string)

print("The original list is:", tup_list)
print("The extracted digits:", digit_list)
