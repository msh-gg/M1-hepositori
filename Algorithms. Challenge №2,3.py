def pascaline(n):
    n -= 1
    line = [1]
    for k in range(max(n, 0)):
        line.append(line[k] * (n - k) // (k + 1))
    print(line)


inp = int(input())  # Ввід номера рядка

pascaline(inp)  # Активаці функції
