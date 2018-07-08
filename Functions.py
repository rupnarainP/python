def python_food():
    width = 80
    text = 'spam and eggs'
    left_margin = (width - len(text)) // 2
    print(' ' * left_margin, text)


def centre_text(*args, sep=' '):
    text = ''
    for arg in args:
        text += str(arg) + sep

    left_margin = (80 - len(text)) // 2
    return " " * left_margin + text


# with open('centred', mode='w') as centred_file:
#     #call function
#     centre_text('spam and eggs', file=centred_file)
#     centre_text('spam, spam and eggs', file=centred_file)
#     centre_text('spam, spam and spam', file=centred_file)
#     centre_text(12, file=centred_file)

#call function
s1 = centre_text('spam and eggs')
s2 = centre_text('spam, spam and eggs')
s3 = centre_text('spam, spam and spam')
s4 = centre_text(12)

print(s1)
print(s2)
print(s3)
print(s4)
