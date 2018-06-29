ip = input("Please enter an IP Address: ")
ip += "."

segNum = 0
dotNum = 0
index = ""
dotIndex = ""
count = 0

if ip == "":
    print("Nothing was entered")

else:
    for i in range(0, len(ip)):
        index = ip[i]

        if index in "0123456789":
            segNum += 1

        elif index == ".":
            dotNum += 1
            count += 1
            print("Segment {0} contains: {1} characters".format(count, segNum))
            segNum = 0

if ip == "." and dotNum != 0:
    print("Segment {0} contains: {1} characters".format(count, segNum))
    print("Number of segments {}".format(dotNum+1))
