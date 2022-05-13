class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def average_grade(self):
        for grade in self.grades.values():
            av_grade = sum(grade) / len(grade)
        return av_grade

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Not a Student!')
            return
        return self.average_grade() < other.average_grade()

    def __str__(self):
        res = f'\nИмя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания:{self.average_grade()}\n' \
              f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\nЗавершенные курсы: {", ".join(self.finished_courses)}'
        return res


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def average_grade(self):
        for grade in self.grades.values():
            av_grade = sum(grade) / len(grade)
        return av_grade

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Not a Lecturer!')
            return
        return self.average_grade() < other.average_grade()

    def __str__(self):
        res = f'\nИмя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.average_grade()}'
        return res

class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'\nИмя: {self.name} \nФамилия: {self.surname}'
        return res


some_student = Student('Ruoy', 'Eman', 'M')
some_student.courses_in_progress += ['Python']
some_student.courses_in_progress += ['Git']
some_student.finished_courses += ['Введение в программирование']

some_student2 = Student('Anton', 'Borisov', 'M')
some_student2.courses_in_progress += ['Python']
some_student2.courses_in_progress += ['Git']
some_student2.finished_courses += ['Введение в программирование']

some_student3 = Student('Anna', 'Alekseeva', 'F')
some_student3.courses_in_progress += ['Python']
some_student3.courses_in_progress += ['Git']

some_reviewer = Reviewer('Some', 'Buddy')
some_reviewer.courses_attached += ['Python']

some_reviewer2 = Reviewer('Jane', 'Ostin')
some_reviewer2.courses_attached += ['Git']

some_reviewer3 = Reviewer('Petr', 'Petrov')
some_reviewer3.courses_attached += ['Java']

some_reviewer.rate_hw(some_student, 'Python', 10)
some_reviewer2.rate_hw(some_student, 'Git', 8)
some_reviewer.rate_hw(some_student, 'Python', 7)
some_reviewer.rate_hw(some_student2, 'Python', 8)
some_reviewer2.rate_hw(some_student2, 'Git', 7)
some_reviewer.rate_hw(some_student2, 'Python', 8)
some_reviewer2.rate_hw(some_student3, 'Git', 9)
some_reviewer.rate_hw(some_student3, 'Python', 6)
some_reviewer.rate_hw(some_student2, 'Python', 8)
some_reviewer2.rate_hw(some_student3, 'Git', 7)
some_reviewer.rate_hw(some_student3, 'Python', 8)

some_lecturer = Lecturer('Ivan' , 'Ivanov')
some_lecturer.courses_attached += ['Python']

some_lecturer2 = Lecturer('Ilon' , 'Mask')
some_lecturer2.courses_attached += ['Python']

some_lecturer3 = Lecturer('Peter' , 'Griffin')
some_lecturer3.courses_attached += ['Python']


some_student.rate_lecturer(some_lecturer, 'Python', 9)
some_student.rate_lecturer(some_lecturer2, 'Python', 8)
some_student.rate_lecturer(some_lecturer3, 'Python', 9)
some_student2.rate_lecturer(some_lecturer, 'Python', 10)
some_student2.rate_lecturer(some_lecturer2, 'Python', 9)
some_student2.rate_lecturer(some_lecturer3, 'Python', 10)

print(some_student.grades)
print(some_lecturer.grades)

print(some_reviewer)
print(some_lecturer)
print(some_student)

student_list = [some_student, some_student2, some_student3]
lecturer_list = [some_lecturer, some_lecturer2, some_lecturer3]

def student_average_grade(list_):
    for student in list_:
        print(f'\nСтудент {student.name} {student.surname}')
        for student.course, student.grade in student.grades.items():
            print(f'по Курсу {student.course} имеет среднюю оценку {sum(student.grade)/len(student.grade)}')

def lecturer_average_grade(list_):
    for lecturer in list_:
        print(f'\nЛектор {lecturer.name} {lecturer.surname}')
        for lecturer.course, lecturer.grade in lecturer.grades.items():
            print(f'по Курсу {lecturer.course} имеет среднюю оценку {sum(lecturer.grade)/len(lecturer.grade)}')

student_average_grade(student_list)
lecturer_average_grade(lecturer_list)

