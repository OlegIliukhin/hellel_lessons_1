# Користувач вводить рядок, Ваше завдання – перетворити рядок на hashtag.
# Декілька правил:
# ніяких символів з набору string.punctuation не повинно бути, у тому числі й пробілів;
# підсумкова довжина hashtag має бути не більше 140 символів.
# кожне слово починається з великої літери.
# якщо довжина фінішного хештегу більше 140 символів - обрізати підсумковий рядок до 140 символів.
# Приклади:
# 1)'Python Community' -> #PythonCommunity
# 2)'i like python community!' -> #ILikePythonCommunity
# 3)'Should, I. subscribe? Yes!' -> #ShouldISubscribeYes
# ******
# text.split() — разбивает строку на слова.
# word.capitalize() — делает первую букву каждого слова большой.
# ''.join(...) — соединяет все слова без пробелов.
# string.punctuation — убирает все знаки препинания.
# [:140] — обрезает до 140 символов.

import string
# 1)
text = "Python Community"
hashtag = '#' + ''.join(word.capitalize() for word in text.split())
# до 140 символов
hashtag = hashtag[:140]
print(hashtag)

# 2)
text = "i like python community!"
