# t = "a", "b", "c"
#
# #Tuple
# print(t)
# #Just strings
# print("a", "b", "c")
# #Tuple
# print(("a", "b", "c"))

#Tuples are immutable

welcome = "Welcome to my Nightmare", "Alice Cooper", 1975
bad = "Bad Company", "Bad Company", 1974
budgie = "Nightlight", "Budgie", 1981
emelda = "More Mayhem", "Emilda May", 2011
metallica = "Ride the ligtning", "Metallica", 1984

print(metallica)
print(metallica[0])
print(metallica[1])
print(metallica[2])


print(emelda)
#Tuples are immutable but you can replace a value within one
emelda = emelda[0], "Imelda May", emelda[2]
print(emelda)

metallica2 = ["Ride the ligtning", "Metallica", 1984]
print(metallica2)
metallica2[0] = "Master of Puppets"
print(metallica2)

title, artist, year = emelda
print(title)
print(artist)
print(year)

#gives an error
# metallica2.append("Rock")
# title, artist, year = metallica2
# print(title)
# print(artist)
# print(year)

emelda = "More Mayhem", "Emilda May", 2011, ((1, "Pulling the Rig"), (2, "Psycho"), (3, "Mayhem"), (4, "Ketish Town Waltz"))
title, artist, year, tracks = emelda
print(emelda)
print(title)
print(artist)
print(year)

for song in tracks:
    #unpacking the tuple of song number and title
    track, title = song
    print("Track number; {0}\t Title: {1} ".format(track, title))






