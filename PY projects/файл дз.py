n = int(input(' Введите количество элементов списка '))
list1 = []
for i in range(n):
    a = int(input(f' Введите число {i + 1} '))
    list1.append(a)
b = 1
for a in list1:
    b += a
f = b /  n
print(f)