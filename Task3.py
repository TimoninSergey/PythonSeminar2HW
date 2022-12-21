""" Реализуйте алгоритм перемешивания списка. 
НЕ ИСПОЛЬЗОВАТЬ ВСТРОЕННЫЕ БИБЛИОТЕКИ SHUFFLE, 
максимум использование библиотеки Random для и получения случайного int
 """

import random    #А как вообще без рандома-то? Откуда-то случайные значения надо брать.

def fill_list ():
    list = []
    list_length = int(input('Введите длину списка: '))
    i = 0
    while i < list_length:
        list.append(input('Введите элемент списка номер {}: '.format(i)))
        i = i+1
    print(list)
    return list

def mix_list (list):
    mixed_list = []
    a = len(list)
    i = 0
    for i in range(a):
        rand_index = random.randint(0, a - 1 - i)
        mixed_list.append(list[rand_index])
        list.remove(list[rand_index])
    print(mixed_list)


mix_list(fill_list())