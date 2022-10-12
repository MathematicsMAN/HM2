# a = int(input(" Введите число 1 "))
# if a > 0:
#     a += 3
# elif a < 0:
#     a -= 2
# else:
#     a += 1
# print(a)

# a = int(input(" Введите число 1 "))
# b = int(input(" Введите число 2 "))
# c = int(input(" Введите число 3 "))
# j, l, v = 0,0,0
# if a < 0:
#     j = 1
# if b < 0:
#     l = 1
# if c < 0:
#     v = 1
# print(j + l + v)


j = 0
for i in range(3):
    a = int(input("Введите число: "))
    if a < 0:
        j += 1
print(f'Число отрицательных чисел: {j}')





