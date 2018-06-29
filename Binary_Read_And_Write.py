# with open("binary", "bw") as file:
#     for i in range(17):
#         file.write(bytes([i])) #needs to converted to a list to be passed to a byte

# #another way of writing it
# with open("binary", "bw") as file:
#     file.write(bytes(range(17))) #needs to converted to a list to be passed to a byte
#
#
# with open("binary", "br") as file:
#     for b in file:
#         print(b)

a = 65534
b = 65535
c = 65537
x = 2998302

with open("binary2", "bw") as bin:
    bin.write(a.to_bytes(2, "big"))
    bin.write(b.to_bytes(2, "big"))
    bin.write(c.to_bytes(4, "big"))
    bin.write(x.to_bytes(4, "big"))
    bin.write(x.to_bytes(4, "little"))

with open("binary2", "br") as bin:
    e = int.from_bytes(bin.read(2), "big")
    print(e)
    f = int.from_bytes(bin.read(2), "big")
    print(f)
    g = int.from_bytes(bin.read(4), "big")
    print(g)
    h = int.from_bytes(bin.read(4), "big")
    print(h)
    i = int.from_bytes(bin.read(4), "big")
    print(i)