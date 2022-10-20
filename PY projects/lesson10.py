# result = 0
# for temp in range(10):
#     if temp % 2 == 0:
#         result += 1
#     else:
#         result -= 1
# print(result)

# for i in range(5):
#     print(i)
#     print("hello")
#     i = i + 10
#     print(i,"Конец цикла")



# result = 0
# for temp in range(10):
#     if temp % 2 == 0:
#         result += 2
#     else:
#         result += 1
# print(result)




# a = int(input(" Введите число 1 "))
# b = int(input(" Введите число 2 "))
# for i in range(a,b + 1):
#     print(i,end=" ")






# a = 0
# for temp in range(5):
#     a += 1
#     if a == 3:
#         a += 2
#     if a == 4:
#         a += 3
#     if a == 5:
#         a += 4
#     else:
#         a += 1
# print(a)





# n = int(input(" Введите число n "))
# n1 = 0
# n2 = 1
# s = n1 + n2
# print(n2,n2, end=" ")
# while s < n:
#     n1,n2 = n2,s
#     s = n1 + n2
#     print(s, end=" ")




n = int(input(" Введите число n "))
x = float(input(" Введите число  x "))
s = 1
t = 1
for i in range(1,n + 1):
    t = t * x / i
    s += t
print(s)
