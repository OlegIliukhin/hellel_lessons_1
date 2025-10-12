# Д.З 4.3
# Створіть список випадкових чисел від 0 до 100 із випадковою кількістю
# елементів від 3 до 10 (для цього використовуйте бібліотеку random)


# ******* решение
# random.randint(3, 10) — визначає, скільки елементів буде у списку.
#
# random.randint(0, 100) — генерує кожне випадкове число.
#
# [ ... for _ in range(n)] — створює список із потрібною кількістю елементів.

import random

# від 3 до 10
n = random.randint(3, 10)
print(n)

# від 0 до 100
numbers = [random.randint(0, 100)
           for _ in range(n)]
print(numbers)

# import random; numbers = [random.randint(0, 100) for _ in range(random.randint(3, 10))]; print(n), print(numbers)
# Вопрос.????? в одну строчку не работает код т.е не показывает количество элиментов, почему  %-(


