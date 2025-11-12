# Створіть клас, що описує людину (створіть метод, що виводить інформацію про людину).
# На його основі створіть клас Студент (перевизначте метод виведення інформації).
# Створіть клас Група, екземпляр якого складається з об'єктів класу Студент.
# Реалізуйте методи додавання, видалення студента та метод пошуку студента на прізвище.
# Метод пошуку студента повинен повертати саме екземпляр класу Студент, якщо студент є у групі, інакше - None.
# У методі видалення, використовуйте результат методу пошуку. Тобто. потрібно скомбінувати ці два методи;)
# Визначте для групи метод str() для повернення списку студентів у вигляді рядка.
# Нижче наведені заготовки, які необхідно доповнити.


from typing import Optional, Set

class Human:
    # Класс описывает человека

    def __init__(self, gender: str, age: int, first_name: str, last_name: str) -> None:
        # Пол, возраст, имя и фамилия
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self) -> str:
        # Возвращаею строку с описанием человека
        return f'{self.first_name} {self.last_name}, {self.gender}, {self.age} y.o.'


class Student(Human):
    # Класс Студент, наследуется от Human

    def __init__(self, gender: str, age: int, first_name: str, last_name: str, record_book: str) -> None:
        # Наследую атрибуты человека
        super().__init__(gender, age, first_name, last_name)
        # Добавляю номер зачетной книжки
        self.record_book = record_book

    def __str__(self) -> str:
        # Возвращает строку с описанием студента
        return f'{self.first_name} {self.last_name}, record book: {self.record_book}'


class Group:
    # Класс Группа, содержит студентов

    def __init__(self, number: str) -> None:
        # Номер группы
        self.number = number
        # Множество студентов (уникальные объекты Student)
        self.group: Set[Student] = set()

    def add_student(self, student: Student) -> None:
        # Добавляет студента в группу
        self.group.add(student)

    def find_student(self, last_name: str) -> Optional[Student]:
        # Ищет студента по фамилии
        # Возвращает объект Student, если найден, иначе None.

        for student in self.group:
            if student.last_name == last_name:
                return student
        return None

    def delete_student(self, last_name: str) -> None:
        # Удаляет студента по фамилии, если он найден
        student = self.find_student(last_name)
        if student:
            self.group.remove(student)

    def __str__(self) -> str:
        # список всех студентов группы
        all_students = ''
        for student in self.group:
            all_students += str(student) + '\n'
        return f'Number:{self.number}\n{all_students}'


st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')

gr = Group('PD1')
gr.add_student(st1)
gr.add_student(st2)

print(gr)
# Number:PD1
# Student: Steve Jobs, record book: AN142
# Student: Liza Taylor, record book: AN145

assert str(gr.find_student('Jobs')) == str(st1), 'Test1'
assert gr.find_student('Jobs2') is None, 'Test2'
assert isinstance(gr.find_student('Jobs'), Student) is True, 'Метод поиска должен возвращать экземпляр'

gr.delete_student('Taylor')
print(gr)  # останется только один студент

gr.delete_student('Taylor')  # повторное удаление без ошибки

print("OK 👌🏻")

