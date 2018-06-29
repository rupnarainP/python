fruit = {"orange" : "a sweet orange citrus fruit",
         "apple" : "good for making cider",
         "lemon" : "a sour, yellow, citrus fruit",
         "grape" : "a small, sweet fruit growing in bunches",
         "lime" : "a sour, green citrus fruit"}

print(fruit)

veg = {"cabbage": "Every child's favourite",
       "sprouts": "mmm, lovely",
       "spinach": "can I have some more fruit please"}

print(veg)

#adds the fruit dictionary to the veg dictionary
veg.update(fruit)
print(veg)

#copy's the fruit dictionary and updates it with veg dictionary without affecting the original dictionaries
nice_and_nasty = fruit.copy()
nice_and_nasty.update(veg)
print(nice_and_nasty)