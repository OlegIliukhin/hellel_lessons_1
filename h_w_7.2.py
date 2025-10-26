# На вхід функції correct_sentence передається речення. Необхідно повернути його виправлену копію так,
# щоб воно завжди починалося з великої літери та закінчувалося крапкою.
# Зверніть увагу, що не всі виправлення необхідні. Якщо речення вже закінчується крапкою,
# додавати ще одну не потрібно, це буде помилкою.
# Вхідні аргументи: string.
# Вихідні аргументи: string.
# Замість pass необхідно написати Ваше рішення.
# def correct_sentence(text):
#     pass
#
import string
def correct_sentence(text):
    if not text:
        return "."
    text = text[0].upper() + text[1:]
    if not text.endswith('.'):
        text += '.'
    return text

print(correct_sentence("greetings, friends"))  # Выведет: Greetings, friends.
print(correct_sentence("hello"))                # Выведет: Hello.
print(correct_sentence("Greetings, friends.")) # Выведет: Greetings, friends.

# ************************
# text[0].upper() + text[1:] — делает первую букву заглавной.
# if not text.endswith('.'): — добавляет точку только если её нет.
# Тесты через assert проверяют работу функции.

def correct_sentence(text):
    # Делаем первую букву заглавной
    text = text[0].upper() + text[1:] if text else ''
    # Добавляем точку в конце, если её нет
    if not text.endswith('.'):
        text += '.'
    return text

assert correct_sentence("greetings, friends") == "Greetings, friends.", 'Test1'
assert correct_sentence("hello") == "Hello.", 'Test2'
assert correct_sentence("Greetings. Friends") == "Greetings. Friends.", 'Test3'
assert correct_sentence("Greetings, friends.") == "Greetings, friends.", 'Test4'
assert correct_sentence("greetings, friends.") == "Greetings, friends.", 'Test5'

print('ОК')


