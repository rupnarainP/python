import shelve

with shelve.open("bike") as bike:
    bike["make"] = "Honda"
    bike["model"] = "250 dream"
    bike["colour"] = "red"
    bike["engine_size"] = 250

    for key in bike:
        print(key)

    print(bike["make"])
    print(bike["colour"])
    print(bike["engine_size"])
