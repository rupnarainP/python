text = input("Enter text: ")

letters = set(text)
print("Original text: {}".format(letters))

#vowels = {"a", "e", "i", "o", "u"}
vowels = frozenset("aeiou")
letters.difference_update(vowels)
print("Answer: {}".format(sorted(letters)))
