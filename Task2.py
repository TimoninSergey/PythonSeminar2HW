""" Задайте список из n чисел последовательности (1 + 1/n)^n, выведеите его на экран, а так же сумму элементов списка.
Пример:
Для n=4 -> [2, 2.25, 2.37, 2.44]
Сумма 9.06 """

def sequence_list_fill (number):
    sequence_list = []
    r = range(1, number+1)
    for i in r:
        sequence_list_element = round((1 + 1/i)**i, 2)
        sequence_list.append(sequence_list_element)
    print(sequence_list)
    return sequence_list

def list_sum_print (list):
    sum = 0
    for element in list:
        sum = sum + element
    print('Сумма списка равна {}'.format(sum))



n = int(input("Задайте натуральное число n: "))

list_sum_print(sequence_list_fill(n))