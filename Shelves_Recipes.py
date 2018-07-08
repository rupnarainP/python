import shelve

# blt = ['bacon', 'lettuce', 'tomato', 'bread']
    # beans_on_toast = ['beans', 'bread']
# scrambled_eggs = ['eggs', 'butter', 'milk']
soup = ['soup']
# pasta = ['pasta', 'cheese']

with shelve.open("recipes", writeback=True) as recipes:
    # recipes['blt'] = blt
    # recipes['beans_on_toast'] = beans_on_toast
    # recipes['scrambled eggs'] = scrambled_eggs
    # recipes['pasta'] = pasta
    #recipes['soup'] = soup

    # #adding to blt(the only way of appending is by using a temp)
    # temp_list = recipes['blt']
    # temp_list.append('butter')
    # recipes['blt'] = temp_list
    #
    # #adding to pasta
    # temp_list = recipes['pasta']
    # temp_list.append('tomato')
    # recipes['pasta'] = temp_list

    #can use writeback=True in the shelve open statement to append without a temp
    #recipes['soup'].append("croutons")

    for snack in recipes:
        print("{} : {}".format(snack, recipes[snack]))