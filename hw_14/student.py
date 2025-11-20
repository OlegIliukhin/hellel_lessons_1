from human import Human


class Student(Human):
    """Класс Студент"""

    def __init__(self, gender: str, age: int, first_name: str, last_name: str, record_book: str) -> None:
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}, record book: {self.record_book}'

    # Метод сравнения
    def __eq__(self, other):
        if not isinstance(other, Student):
            return False
        return str(self) == str(other)

    # ЧтобыStudent можно было хранить в set
    def __hash__(self):
        return hash(str(self))
