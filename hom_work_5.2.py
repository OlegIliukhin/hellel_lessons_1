 # Модифікувати калькулятор таким чином, щоб він працював доти, доки користувач цього хоче.
 # Тобто, потрібно робити запит до користувача на продовження роботи калькулятора після кожного обчислення
 # - якщо користувач ввів yes (можна просто y), то нове обчислення, інакше - закінчення роботи.

import math
num1 = float(input("введите цифру"))
operation = input("выбрать дейсвие (+, -, *, /): ")
num2 = float(input("ввести цифру"))

if operation == "+":
     result = num1 + num2
     print(result)
elif operation == "-":
     result = num1 - num2
     print(result)

elif operation == "*":
     result = num1 * num2
     print(result)

elif operation == "/":
     if num2 == 0:
         print("делить на 0 нельзя!")
     else:
         result = num1 / num2
         print(result)
else:
    print("выбрать дейсвие (+, -, *, /)" )

     again = input("Хотите продолжить? (y/n): ")
     if again.lower() != "y":
         num1 = while True:
             num1 = float(input("введите цифру"))
         else:
    break:


