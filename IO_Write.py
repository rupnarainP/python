cities = ["Durban", "Johannesburg", "Roodepoort", "Cape Town"]

with open("/home/dax/PycharmProjects/python/cities.txt", "w") as file:
    for city in cities:
        print(city, file=file)

cities = []

with open("/home/dax/PycharmProjects/python/cities.txt", "r") as file:
    for city in file:
        cities.append(city)


for city in cities:
    print(city, end="")
