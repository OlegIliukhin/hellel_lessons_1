# Ваше завдання написати функцію, яка прочитає заданий файл, очистить текст від html-тегів
# і запише цей текст в інший файл.
# html-тег завжди починається з "<" і закінчується на ">" тобто.
# потрібно видалити ці символи та все, що між ними.
# Функція отримує на вхід два параметри – ім'я файлу, який потрібно очистити,
# та ім'я файлу, куди потрібно записати очищений текст. Ім'я файлу, куди потрібно писати,
# можна задати за замовчуванням.
# Приклади файлів у вкладенні – файл який потрібно очистити (draft.html) та приклад файлу,
# який може вийти на виході з очищеним текстом (cleaned.txt).
# Файл draft.html необхідно скачати і покласти поряд з файлом, де буде вирішення цієї домашки.
# Додаткове завдання для тих, хто захоче ускладнити рішення - спробуйте прибрати рядки, в яких немає інформації.
#

import codecs
from typing import Optional
# Читає html-файл, видаляє всі html-теги і записує чистий текст у інший файл

def delete_html_tags(html_file: str, result_file: str = 'cleaned.txt') -> None:


    with codecs.open(html_file, 'r', 'utf-8') as file:
        html = file.read()

    cleaned_text = ''
    inside_tag = False

    for char in html:
        if char == '<':
            inside_tag = True
            continue
        if char == '>':
            inside_tag = False
            continue

        if not inside_tag:
            cleaned_text += char

    # удаляю пустые рядки
    cleaned_lines = []
    for line in cleaned_text.split('\n'):
        if line.strip():
            cleaned_lines.append(line)

    result = "\n".join(cleaned_lines)

    with codecs.open(result_file, 'w', 'utf-8') as output:
        output.write(result)


# вызов функции
delete_html_tags("draft.html", "cleaned.txt")
print("Файл очищено!")
