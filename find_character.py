# input
word_list = ['hello','world','my','name','is','Anna']
char = 'o'
output = []


def find_character(list, character):
    for word in word_list:
        if word.find(char) != -1:
            output.append(word)
    print output

find_character(word_list, char)