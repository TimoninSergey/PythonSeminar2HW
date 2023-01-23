""" Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
Пример:
6782 -> 23
0,56 -> 11 """

def number_sum(number):
    number_digits_only = ''.join(filter(lambda i: i is not ',', number))
#    for char in number:
#        if char.isdigit():
#            number_digits_only = number_digits_only + char
    sum = 0
    for char in number_digits_only:
        sum = sum + int(char)
    print(sum)

string_num = input('Введите вещественное число: ')

number_sum(string_num)