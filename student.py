import datetime

class RecordBook:
    def __init__(self, subject, exam_date, teacher_name, grade):
        self.subject = subject
        self.exam_date = exam_date
        self.teacher_name = teacher_name
        self.grade = grade

class Student:
    def __init__(self, last_name, first_name, birth_date, record_book):
        self.last_name = last_name
        self.first_name = first_name
        self.birth_date = birth_date
        self.record_book = record_book  # список записей в зачетке

    def average_grade(self):
        return sum(record.grade for record in self.record_book) / len(self.record_book)

students = [
    Student("Иванов", "Иван", datetime.date(2000, 1, 15), [
        RecordBook("Математика", datetime.date(2023, 1, 15), "Петров В.В.", 5),
        RecordBook("Физика", datetime.date(2023, 1, 20), "Сидоров А.А.", 4),
        RecordBook("История", datetime.date(2023, 1, 25), "Иванова О.О.", 5)
    ]),
    Student("Петров", "Петр", datetime.date(1999, 2, 20), [
        RecordBook("Математика", datetime.date(2023, 1, 15), "Петров В.В.", 4),
        RecordBook("Физика", datetime.date(2023, 1, 20), "Сидоров А.А.", 5),
        RecordBook("История", datetime.date(2023, 1, 25), "Иванова О.О.", 5)
    ]),
    Student("Сидоров", "Сидор", datetime.date(2001, 3, 10), [
        RecordBook("Математика", datetime.date(2023, 1, 15), "Петров В.В.", 3),
        RecordBook("Физика", datetime.date(2023, 1, 20), "Сидоров А.А.", 4),
        RecordBook("История", datetime.date(2023, 1, 25), "Иванова О.О.", 4)
    ]),
]

def best_student(students):
    best = max(students, key=lambda s: s.average_grade())
    return best

best = best_student(students)
print(f"Лучший студент: {best.last_name} {best.first_name}")
for record in best.record_book:
    print(f"Предмет: {record.subject}, Оценка: {record.grade}, Преподаватель: {record.teacher_name}, Дата экзамена: {record.exam_date}")
