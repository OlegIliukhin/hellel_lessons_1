# Напишіть функцію common_elements, яка згенерує два списки елементів з генераторного виразу (range) для 100 елементів, за наступними правилом:
# Один список з числами кратними 3, інший з кратними числами 5.
# За допомогою множин створіть набір з числами, які є в обох множинах (перетин).
# Функція повинна повернути цю множину як результат своєї роботи.
#
#
# ********* для себя
set3 = {i for i in range(100) if i % 3 == 0}  # кратные 3
set5 = {i for i in range(100) if i % 5 == 0}  # кратные 5

result = set3.intersection(set5)

print(result)

# решение ДЗ
def common_elements():
    set3 = {i for i in range(100) if i % 3 == 0}
    set5 = {i for i in range(100) if i % 5 == 0}
    return set3.intersection(set5)

assert common_elements() == {0, 75, 45, 15, 90, 60, 30}
print('OK')



