def second_index(text, some_str):
    # Ищем первое вхождение
    i = text.find(some_str)
    if i == -1:
        return None
    # Ищем второе вхождение после первого
    i = text.find(some_str, i + 1)
    return i if i != -1 else None

# Тесты
assert second_index("sims", "s") == 3, 'Test1'
assert second_index("find the river", "e") == 12, 'Test2'
assert second_index("hi", "h") is None, 'Test3'
assert second_index("Hello, hello", "lo") == 10, 'Test4'

print('ОК')
# **************
def second_index(text, some_str):
    i = text.find(some_str)
    if i == -1:
        return None
    i = text.find(some_str, i + 1)
    return i if i != -1 else None

print(second_index("find the river", "e"))  # Ожидается: 3
