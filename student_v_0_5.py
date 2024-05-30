import datetime

class Student:
    def __init__(self, last_name, first_name, birth_date, grades):
        self.last_name = last_name
        self.first_name = first_name
        self.birth_date = birth_date
        self.grades = grades  # список предметов и оценок

    def average_grade(self):
        return sum(grade for _, grade in self.grades) / len(self.grades)

students = [
    Student("Иванов", "Иван", datetime.date(2000, 1, 15), [("Математика", 5), ("Физика", 4), ("История", 5)]),
    Student("Петров", "Петр", datetime.date(1999, 2, 20), [("Математика", 4), ("Физика", 5), ("История", 5)]),
    Student("Сидоров", "Сидор", datetime.date(2001, 3, 10), [("Математика", 3), ("Физика", 4), ("История", 4)]),
]

def best_student(students):
    best = max(students, key=lambda s: s.average_grade())
    return best

best = best_student(students)
print(f"Лучший студент: {best.last_name} {best.first_name}")
for subject, grade in best.grades:
    print(f"Предмет: {subject}, Оценка: {grade}")
