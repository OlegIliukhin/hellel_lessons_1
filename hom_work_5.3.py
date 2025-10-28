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
# 1) #PythonCommunity
text = "Python Community"
hashtag = "#" + "".join(word.capitalize() for word in text.split())
# до 140 символов
hashtag = hashtag[:140]
print(hashtag)

# 2) #ILikePythonCommunity
text = "i like python community!"
hashtag = "#" + "".join(word.capitalize() for word in text.split())
#  "#" не трогаем
hashtag = "#" + "".join(c for c in hashtag[1:] if c not in string.punctuation)
hashtag = hashtag[:140]
print(hashtag)

# 3) #ShouldISubscribeYes
text = "Should, I. subscribe? Yes!"
hashtag = '#' + ''.join(word.capitalize() for word in text.split())
hashtag = '#' + ''.join(c for c in hashtag[1:] if c not in string.punctuation)
hashtag = hashtag[:140]

print(hashtag)


# ***********

def make_hashtag():
    text = input("Введіть рядок: ")
    # убераем все знаки
    for s in string.punctuation:
        text = text.replace(s, "")
    # делаем с большой буквы
    words = text.split()
    hashtag = "#" + "".join(word.capitalize() for word in words)
    # обризаем
    return hashtag[:140]

print(make_hashtag())
