students_list = []
lectors_list = []


class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        global students_list
        students_list += [self]

    def __str__(self):
        print(f'Имя: {self.name}\nФамилия: {self.surname}\nПол: {self.gender}')
        print(f'Средняя оценка за домашние задания: {self.average_grade()}')
        print(f'Курсы в процессе обучения: {", ".join(str(i) for i in self.courses_in_progress)}')
        return f'Завершенные курсы: {", ".join(str(i) for i in self.finished_courses)}\n'

    def __lt__(self, other):
        print(f'Процесс сравнения {self.name} с {other.name} запущен.')
        print(f'{self.name} лучше {other.name}?')
        print(f'Значения: {self.name} - {self.average_grade()}, {other.name} - {other.average_grade()}.')
        if self.average_grade() < other.average_grade():
            answer = 'Нет!'
        else:
            answer = 'Да!'
        return f'Ответ: {answer}\n'

    def rate_qe(self, lecturer, course, grade):
        if 0 <= grade <= 10:
            if isinstance(lecturer, Lecturer) and \
                    (course in self.courses_in_progress or course in self.finished_courses) and \
                    course in lecturer.courses_attached:
                if course in lecturer.grades:
                    lecturer.grades[course] += [grade]
                else:
                    lecturer.grades[course] = [grade]
            else:
                return print('Ошибка')
        else:
            return print('Оценка не находится в пределах от 0 до 10')

    def average_grade(self):
        amount = 0
        k = 0
        for i in self.grades.keys():
            for j in self.grades.get(i):
                amount += j
                k += 1
        result = amount / k
        return result


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        global lectors_list
        lectors_list += [self]

    def __str__(self):
        print(f'Имя: {self.name}')
        print(f'Фамилия: {self.surname}')
        return f'Средняя оценка за лекции: {self.average_grade()}\n'

    def __lt__(self, other):
        print(f'Процесс сравнения {self.name} с {other.name} запущен.')
        print(f'{self.name} лучше {other.name}?')
        print(f'Значения: {self.name} - {self.average_grade()}, {other.name} - {other.average_grade()}.')
        if self.average_grade() < other.average_grade():
            answer = 'Нет!'
        else:
            answer = 'Да!'
        return f'Ответ: {answer}\n'

    def average_grade(self):
        amount = 0
        k = 0
        for i in self.grades.keys():
            for j in self.grades.get(i):
                amount += j
                k += 1
        result = amount / k
        return result


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if 0 <= grade <= 10:
            if isinstance(student, Student) and course in self.courses_attached and \
                    course in student.courses_in_progress:
                if course in student.grades:
                    student.grades[course] += [grade]
                else:
                    student.grades[course] = [grade]
            else:
                return 'Ошибка'
        else:
            return print('Оценка не находится в пределах от 0 до 10')

    def __str__(self):
        print(f'Имя: {self.name}')
        return f'Фамилия: {self.surname}\n'


def average_grade(list_, course):
    amount = 0
    k = 0
    result = 0
    if 'Student' in str(type(list_[0])):
        class_ = 'студентов'
    else:
        class_ = "лекторов"
    for i in list_:
        if course in i.grades:
            for j in i.grades.get(course):
                amount += j
                k += 1
            result = amount / k
        else:
            continue
    print(f'\nСредняя оценка среди {class_} {", ".join(str(i.name) for i in list_)} по курсу "{course}": {result}')


# Init instance
student_01 = Student('Harry', 'Potter', 'male')
student_02 = Student('Hermione', 'Granger', 'female')
lecturer_01 = Lecturer('Oleg', 'Bulygin')
lecturer_02 = Lecturer('Evgeny', 'Shmargunov')
reviewer_01 = Reviewer('Andrey', 'Semakin')
reviewer_02 = Reviewer('Roman', 'Alexeev')

# Init finished courses
student_01.finished_courses += ['Git']

# Init courses in progress
student_01.courses_in_progress += ['Python']
student_02.courses_in_progress += ['Git', 'Python']

# Init mentor's courses attached
lecturer_01.courses_attached += ['Python']
lecturer_02.courses_attached += ['Git']
reviewer_01.courses_attached += ['Python']
reviewer_02.courses_attached += ['Git']

# Init rating
reviewer_01.rate_hw(student_01, 'Python', 10)
reviewer_01.rate_hw(student_02, 'Python', 6)
reviewer_02.rate_hw(student_01, 'Git', 7)
reviewer_02.rate_hw(student_02, 'Git', 9)
student_01.rate_qe(lecturer_01, 'Python', 10)
student_01.rate_qe(lecturer_02, 'Git', 5)
student_02.rate_qe(lecturer_01, 'Python', 10)
student_02.rate_qe(lecturer_02, 'Git', 8)

# Show all people
print(student_01)
print(student_02)
print(lecturer_01)
print(lecturer_02)
print(reviewer_01)
print(reviewer_02)

# Fight!
print(lecturer_01 < lecturer_02)
print(lecturer_02 < lecturer_01)
print(student_01 < student_02)
print(student_02 < student_01)

# Average grade
average_grade(students_list, 'Python')
average_grade(students_list, 'Git')
average_grade(lectors_list, 'Python')
average_grade(lectors_list, 'Git')
