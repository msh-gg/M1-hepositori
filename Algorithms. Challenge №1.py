#Реалізувати програму, яка читає дані з текстового файлу і записує їх в інший текстовий файл у
#зворотньому порядку. Шлях до файлу повинен прийматись програмою як вхідний параметр.
#Програма повинна коректно поводитись у випадку, якщо файлу не існує.

import os

filename = input("Введіть шлях до файлу: ")
if not os.path.exists(filename):
    print("Вказаного файлу не існує")
else:
    with open(filename , encoding = "utf8") as file:
        indata = (file.read())
    with open('pit.txt' , 'w+', encoding = "utf8") as output_file:
        output_file.write(indata[::-1])
    print('delo sdelano')
