# первое задание 3 урока

# создание функции переводчика
dict_of_words = {'один': 'one', 'два': 'two', 'три': 'three', 'четыре': 'four', 'пять': 'five',
                 'шесть': 'six', 'семь': 'seven',
                 'восемь': 'eight', 'девять': 'nine', 'десять': 'ten'}


def num_translate(get_word):
    my_list = []
    my_list = list(get_word)
    get_word = str(get_word.lower())
    if 64 < ord(my_list[0]) < 91 or 96 < ord(my_list[0]) < 123:
        for key, values in dict_of_words.items():
            if values == get_word:
                print('На русском языке:', key.capitalize() if str(my_list[0]).isupper() else key)
    elif 1039 < ord(my_list[0]) < 1104:
        print('На английском языке:',
              dict_of_words.get(get_word).capitalize()
              if str(my_list[0]).isupper()
              else dict_of_words.get(get_word))

    else:
        return None


num_translate(str(input("Введите чиcло для перевода: ")))

# print(ord('1'))
# i = 0
# while i < 64:
#      i+=1
#      print(chr(i+1039), i+1039)
