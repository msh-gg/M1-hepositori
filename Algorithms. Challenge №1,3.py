def angle(x1, y1, x2, y2):
    xo = 0
    yo = 0
    k1 = abs((y1 - yo) / (x1 - xo))     # Обчислення кутового коефіієнта для ОА
    k2 = abs((y2 - yo) / (x2 - xo))     # Обчислення кутового коефіієнта для ОВ

    if k1 >= k2:
        print("OA")
    else:
        print("OB")


x1, y1, x2, y2 = map(int, input().split(" "))   # Ввід координат

angle(x1, y1, x2, y2)   # Запуск функції
