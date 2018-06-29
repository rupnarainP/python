# file = open("/home/dax/PycharmProjects/python/sample.txt", "r")
#
# for line in file:
#     print(line, end="")
#
# file.close()

# #better way of open files as it handles errors for you
# with open("/home/dax/PycharmProjects/python/sample.txt", "r") as file:
#     for line in file:
#         print(line, end="")

# with open("/home/dax/PycharmProjects/python/sample.txt", "r") as file:
#     line = file.readline()
#     while line:
#         print(line, end="")
#         line = file.readline()

with open("/home/dax/PycharmProjects/python/sample.txt", "r") as file:
    lines = file.readlines()
    #stores the entire text file as a list of strings
print(lines)

for line in lines:
    print(line, end="")
