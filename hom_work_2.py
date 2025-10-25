#  ДЗ 2.1
number = int(input("Введіть 4-значне число: "))

# находим каждую цифру
a = number // 1000              # перша цифра
b = (number // 100) % 10        # друга цифра
c = (number // 10) % 10         # третя цифра
d = number % 10                 # четверта цифра
# печатаем цифры столбиком
print(a)
print(b)
print(c)
print(d)

number = int(input("Введіть 5-значне число: "))
a = number // 10000
b = (number // 1000) % 10
c = (number // 100) % 10
d = (number // 100) % 10
e = number % 10

print(a)
print(b)
print(c)
print(d)
print(e)

# ДЗ 2.2
number = int(input("Введіть 5-значне число: "))

a = number // 10000
b = (number // 1000) % 10
c = (number // 100) % 10
d = (number // 10) % 10
e = number % 10
print(e,d,c,b,a)
# печатаем от последней цифре к первой (реверс)
reversed_number = e * 10000 + d * 1000 + c * 100 + b * 10 + a
print(reversed_number)
