"""
    File: writer_bot.py
    Author: Jake Kravas
    Purpose: 
"""

import random

def get_data():
    # sfile = input()
    # n = input() #prefix size
    # words_to_generate = int(input())

    sfile = '../bee.txt'
    n = 2
    words_to_generate = 50

    words = [] # words in file

    sfile_data = open(sfile, 'r')
    sfile_lines = sfile_data.readlines()

    for line in sfile_lines:
        line = line.strip()
        line_words = line.split()
        for word in line_words:
            words.append(word)
    
    prefix_dict = {('NONWORD', 'NONWORD'): [words[0]], ('NONWORD', words[0]): [words[1]]}

    for i in range(len(words)):
        if i + n < len(words):

            prefix = tuple(words[i:i + n])

            if prefix in prefix_dict:
                prefix_dict[prefix].append(words[i + n])
            else:
                prefix_dict[prefix] = [words[i + n]]
    
    return prefix_dict, n, words_to_generate


def generate_text(prefix_dict, n, words_to_generate):

    # prefix_list = prefix_dict.keys()
    prefix_list = list(prefix_dict)
    # print(prefix_dict)
    count = 0

    # words_to_display = [word for word in prefix_list[0]]
    words_to_display = []

    # getting n amount of words into words_to_display to start
    for p in prefix_list:
        if len(words_to_display) < n:
            new_word = prefix_dict[p][0]
            words_to_display.append(prefix_dict[p][0])


    cur_word_list = prefix_dict[tuple(words_to_display[-n:])]
    cur_prefix_tup = tuple(words_to_display[-n:])
    
    while cur_prefix_tup in prefix_dict and len(words_to_display) < words_to_generate:
        cur_word_list = prefix_dict[cur_prefix_tup]
        rand_num = random.randint(0, len(cur_word_list)-1)

        new_word = cur_word_list[rand_num]
        words_to_display.append(new_word)

        cur_prefix_tup = tuple(words_to_display[-n:])


    



    # while len(words_to_display) < words_to_generate or not tuple(cur) in prefix_dict:
    # while len(words_to_display) < words_to_generate and tuple(cur) in prefix_dict:
    # while len(words_to_display) < words_to_generate:
        # if len(cur) == 1:
        # print(tuple(cur) in prefix_dict)
        # words_to_display.append(cur[0])
        # cur = prefix_dict[tuple(words_to_display[-n:])]
    # print(words_to_display)





    # print(n)
    # print(words_to_display)
    # print(tuple(words_to_display[-n:]))


    # for i in range(n):
    #     words_to_display

    # while len(words_to_display) < n:
    #     for pref in prefix_dict:
    #         print(pref)
    #         words_to_display.append('a')


    # for pref in prefix_dict:
    #     # while len(words_to_display) < n:
    #     #     print(pref)

    #     if len(words_to_display) < 2:
    #         words_to_display.append(prefix_dict[pref])

    # print(words_to_display)

    # cur = prefix_dict[prefix_list[0]]
    # cur = prefix_dict[prefix_list]

    # while count < words_to_generate:
    #     if words_to_display
    #     words_to_display.append(cur[0])
    #     # cur = 
    #     count += 1


    # for m in prefix_dict:
    #     print(m)

    # print(prefix_dict)


    # print(prefix)

    # print(' '.join(prefix))
    # print(prefix[-1])

    # print(prefix_dict[prefix])

    # while count < words_to_generate:
    #     for word in prefix:
    #         words_to_display.append(word)
        
        # words_to_display.append(' '.join(prefix))


    # for i in range(words_to_generate):
    #     print(prefix_dict[prefix_list[i]])

    # while count < words_to_generate:
    #     words_to_display.append(cur)

    #     if len(cur) == 1:
    #         words_to_display.append(cur[0])

    #     count += 1




    # while count < words_to_generate:
        # print(words_to_display)

        # words_to_display += 


        # if len(prefix) > 1:
        #     print('AAA')
        #     for word in prefix:
        #         words_to_display.append(word)
        #     if len(prefix_dict[prefix]) == 1:
        #         prefix = tuple(prefix_dict[prefix][0])

        # count += 1




        # for prefix in prefix_tup:
        #     print(prefix)

    # for i in range(words_to_generate):
    #     if i == 0:
    #         print(' '.join(first_prefix))
        # print(i)



def main():
    prefix_dict, n, words_to_generate = get_data()
    generate_text(prefix_dict, n, words_to_generate)

main()