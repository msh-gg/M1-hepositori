n = int(input())   # Кількість масивів які приймає програма

arr = [[] for _ in range(n)]   # Двохвимірний масив який буде містити дані масиви
arrf = []                      # Масив в якому будуть поєднані дані масиви
arrRes = []


for i in range(n):
    s = input()
    arr[i] = [int(x) for x in s.split()]    # Считування масивів
    s = 0

    arrf += arr[i]  # Об'єднання даних масивів в один

arrf.sort()

for x in arrf:
    if x % 5 != 0:  # Видалення чисел кратних 5
        arrRes.append(x)

print(arrRes)