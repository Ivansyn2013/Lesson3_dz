# домашнее задание №5 третьего урока

# Реализовать функцию get_jokes(), возвращающую n шуток, сформированных
# из трех случайных слов, взятых из трёх списков (по одному из каждого):
import random


def get_jokes(n):
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
    i = 0
    while i < n:
        resul_list = []
        resul_list.append(nouns[random.randrange(0, len(nouns), 1)])
        resul_list.append(adverbs[random.randrange(0, len(adverbs), 1)])
        resul_list.append(adjectives[random.randrange(0, len(adjectives), 1)])
        print(' '.join(resul_list))
        i += 1


get_jokes(int(input("Введи число:")))
