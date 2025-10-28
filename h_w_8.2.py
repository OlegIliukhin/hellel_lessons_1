# Ваше завдання – написати функцію is_palindrome, яка перевірятиме, чи є рядок паліндромом.
# Паліндромом - це такий рядок, який читається однаково зліва направо і зправа наліво без урахування знаків пунктуації та розмірності букв.
# Функція приймає на вхід рядок, та повертає булеве значення True або False
# игнорировать знаки пунктуации
# игнорировать регистр букв (A == a)
# делаю строку в нижнем регистру
# text.lower()
#
# ch.isalnum() Удалить все знаки пунктуации и пробелы возвращает True, если символ — буква или цифра.
# cleaned = ''.join(ch.lower() for ch in text if ch.isalnum())
#
# Проверить, совпадает ли строка с перевёрнутой:
# cleaned == cleaned[::-1]

# Приклад:
def is_palindrome(text):
    cleaned = ''.join(ch.lower() for ch in text if ch.isalnum())
    return cleaned == cleaned[::-1]

assert is_palindrome('A man, a plan, a canal: Panama') == True, 'Test1'
assert is_palindrome('0P') == False, 'Test2'
assert is_palindrome('a.') == True, 'Test3'
assert is_palindrome('aurora') == False, 'Test4'
print("ОК")
