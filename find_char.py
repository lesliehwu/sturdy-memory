def find_char(some_list,the_letter): #some_list is a list. the_letter is a character
    new_list = []
    for el in some_list:
        if(el.find(the_letter) >= 0):
            new_list.append(el)

    return new_list

word_list = ["hello","world","my","name","is","Anna"]
char = 'o'

print(find_char(word_list,char))
