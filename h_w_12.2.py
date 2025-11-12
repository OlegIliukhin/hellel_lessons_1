# Створіть клас для опису товару (припустимо, це заділ для інтернет-магазину). Як поля товару можете використовувати значення ціни, опис, габарити товару. Створіть пару екземплярів вашого класу та протестуйте їхню роботу.
# Створіть клас "Покупець". Як поля можна використовувати прізвище, ім'я, по батькові, мобільний телефон і т.д.
# Створіть клас "Замовлення". Замовлення може містити кілька товарів, причому кількість кожного з товарів може бути різною. Замовлення має бути "підв'язане" до користувача, який його здійснив. Реалізуйте метод обчислення сумарної вартості замовлення. Визначте метод str() для коректного виведення інформації про це замовлення.

# Класс Товар
# class Item:
#     def __init__(self, name, price, description, dimensions):
#         self.name = name          # название товара
#         self.price = price        # цена
#         self.description = description
#         self.dimensions = dimensions
#
#     def __str__(self):
#         # строковое представление товара
#         return f"{self.name}, price: {self.price}"
#
#
# # Класс Покупатель
# class User:
#     def __init__(self, name, surname, phone):
#         self.name = name
#         self.surname = surname
#         self.phone = phone
#
#     def __str__(self):
#         # строковое представление покупателя
#         return f"{self.name} {self.surname}"
#
#
# # Класс Покупка / Корзина
# class Purchase:
#     def __init__(self, user):
#         self.user = user
#         self.products = {}   # словарь: товар - количество
#
#     def add_item(self, item, count):
#         # добавляем товар и количество
#         self.products[item] = count
#
#     def get_total(self):
#         # считаем общую стоимость: цена * количество
#         total = 0
#         for item, count in self.products.items():
#             total += item.price * count
#         return total
#
#     def __str__(self):
#         # вывод всей информации о заказе
#         text = f"User: {self.user} Items:"
#         for item, count in self.products.items():
#             text += f"{item.name}: {count} pcs."
#         return text

class Item:
    def __init__(self, name, price, description, dimensions):
        self.name = name
        self.price = price
        self.description = description
        self.dimensions = dimensions

    def __str__(self):
        return f"{self.name}, price: {self.price}"


class User:
    def __init__(self, name, surname, numberphone):
        self.name = name
        self.surname = surname
        self.numberphone = numberphone

    def __str__(self):
        return f"{self.name} {self.surname}"


class Purchase:
    def __init__(self, user):
        self.user = user
        self.products = {}

    def add_item(self, item, cnt):
        self.products[item] = cnt

    def get_total(self):
        total = 0
        for item, cnt in self.products.items():
            total += item.price * cnt
        return total

    def __str__(self):
        text = f"User: {self.user}\nItems:\n"
        for item, cnt in self.products.items():
            text += f"{item.name}: {cnt} pcs.\n"
        return text

lemon = Item('lemon', 5, "yellow", "small", )
apple = Item('apple', 2, "red", "middle", )
print(lemon)  # lemon, price: 5

buyer = User("Ivan", "Ivanov", "02628162")
print(buyer)  # Ivan Ivanov

cart = Purchase(buyer)
cart.add_item(lemon, 4)
cart.add_item(apple, 20)
print(cart)
"""
User: Ivan Ivanov
Items:
lemon: 4 pcs.
apple: 20 pcs.
"""
assert isinstance(cart.user, User) is True, 'Екземпляр класу User'
assert cart.get_total() == 60, "Всього 60"
assert cart.get_total() == 60, 'Повинно залишатися 60!'
cart.add_item(apple, 10)
print(cart)
"""
User: Ivan Ivanov
Items:
lemon: 4 pcs.
apple: 10 pcs.
"""

assert cart.get_total() == 40