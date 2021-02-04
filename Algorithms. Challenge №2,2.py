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
