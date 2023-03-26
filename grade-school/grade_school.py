from collections import defaultdict
from typing import Union
class School:


    def __init__(self):
        self.students = defaultdict(set)
        self.add_attempts = []

    def add_student(self, name: str, grade: int) -> Union[str, None]:
        if any(name in names for names in self.students.values()):
            self.add_attempts.append(False)
            return f"Name {name} already exists in the school"
        self.add_attempts.append(True)
        self.students[grade].add(name)

    def roster(self) -> list[int]:
        out = []
        for i in sorted(self.students.keys()):
            out += self.grade(i)
        return out

    def grade(self, grade_number: int) -> list[str]:
        return sorted(self.students[grade_number])

    def added(self) -> list[bool]:
        return self.add_attempts
