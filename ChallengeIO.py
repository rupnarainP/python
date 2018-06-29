with open("/home/dax/PycharmProjects/python/sample.txt", "a") as file:
    for i in range(1, 13, 1):
        print("{}\t times \t{} is \t{}".format(i, 2, i * 2), file=file)