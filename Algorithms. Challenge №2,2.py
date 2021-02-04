#3.	Реалізувати програму, яка приймає на вхід три параметри - слово, режим роботи, шлях до текстового файлу. Програма повинна коректно поводить у випадку, якщо файлу не існує. Програма повинна порахувати кількість згадувань введеного слова в файлі та вивести цю кількість на екран. Слово вважається згаданим в залежності від режиму роботи:
#1 (режим за замовчуванням) - пошук часткових співпадінь. Наприклад слово “зуб” вважається згаданим в таких уривках тексту:
#“мене болить зуб”
#“зубр біжить галявиною”
#“зазубрений ніж”
#2 - пошук точних співпаінь слів. Наприклад згадування слова “зуб” вважається:
#“мене болить зуб” - зараховано
#“зубр біжить галявиною” - не зараховано (зуб - частина слова зубр, а не окреме слово)
#“зазубрений ніж”- не зараховано (зуб - частина слова зазубрений, а не окреме слово)


import os


def read_file(word, method, file_path):
    count = 0
    list = []
    with open(file_path,  encoding="utf8") as f:          # Читання файла і передання данних з файла в масив
        for i in f.readlines():
            list.append(i.split())

    if method == "default":             # Якщо режим за замовчуванням
        for i in list:
            for j in i:
                if word in j:
                    count += 1

    if method == "accurate":            # Якщо режим точних співпадінь
        for i in list:
            if word in i:
                count += 1

    print("Word '", word, "' was recognised ", count, " times")     # Вивід результату
    print()

def find_file(word, method, file_path):     # Перевіряє чи існує файл
    if os.path.exists(file_path):
        read_file(word, method, file_path)  # Якщо існує то запускає функцію яка читає файл
    else:
        print("file is not exist")          # кщо не існує виводить повідомлення
        

wordi = input("Enter word: ")
methodi = input("Enter method(default/accurate): ")
pathi = input("Enter path to file: ")

find_file(wordi, methodi, pathi)
