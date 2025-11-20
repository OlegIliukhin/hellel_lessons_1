from typing import Optional, Set
from student import Student


class Group:
    """Класс Группа"""

    def __init__(self, number: str) -> None:
        self.number = number
        self.group: Set[Student] = set()

    def add_student(self, student: Student) -> None:
        self.group.add(student)

    def find_student(self, last_name: str) -> Optional[Student]:
        for student in self.group:
            if student.last_name == last_name:
                return student
        return None

    def delete_student(self, last_name: str) -> None:
        student = self.find_student(last_name)
        if student:
            self.group.remove(student)

    def __str__(self) -> str:
        result = f'Number: {self.number}\n'
        for st in self.group:
            result += str(st) + '\n'
        return result
