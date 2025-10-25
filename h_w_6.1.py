# Користувач вводить через дефіс дві літери, Ваше завдання написати програму, яка повертатиме всі символи між ними включно.
# Жодних перевірок на помилку робити не треба, мінімальне значення завжди менше або дорівнює максимальному.
# Підказка: Використовуйте модуль string , у якому є string.ascii_letters, з усім набором потрібних букв
# Приклад:
# 1) "a-c" -> abc
# 2) "a-a" -> a
# 3) "s-H" -> stuvwxyzABCDEFGH
# 4) "a-A" -> abcdefghijklmnopqrstuvwxyzA

import string

# 1)
s = "a-c"
print(string.ascii_letters[string.ascii_letters.index(s[0]):string.ascii_letters.index(s[2])+1])

# 2)
s = "a-a"
print(string.ascii_letters[string.ascii_letters.index(s[0]):string.ascii_letters.index(s[2]) + 1])

# 3)
s = "s-H"
print(string.ascii_letters[string.ascii_letters.index(s[0]):string.ascii_letters.index(s[2])+1])

# 4)
s = "a-A"
print(string.ascii_letters[string.ascii_letters.index(s[0]):string.ascii_letters.index(s[2])+1])

