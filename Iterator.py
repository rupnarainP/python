# string = "123456789"
#
# iterator = iter(string)
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for num in list1:
    print(num, end='')

iterator = iter(list1)
print()
for i in range(0, len(list1)):
    print(next(iterator), end='')
