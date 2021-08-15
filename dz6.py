class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_courses(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in cool_lecturer.study_course and course in self.courses_in_progress:
            if course in lecturer.course_grades:
                lecturer.course_grades[course] += [grade]
            else:
                lecturer.course_grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Студент \n' \
               f'Имя: {self.name} \n' \
               f'Фамилия: {self.surname} \n' \
               f'Средняя оценка за домашние задания: {self.student_average_rating()} \n' \
               f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)} \n' \
               f'Завершенные курсы: {" ".join(self.finished_courses)}'

    def student_average_rating(self):
        val_list = []
        for val in self.grades.values():
            val_list += val
        return round((sum(val_list)/len(val_list)), 2)

    def __gt__(self, other_student):
        if not isinstance(other_student, Student):
            print('Такого студента нет')
            return
        else:
            if self.student_average_rating() > other_student.student_average_rating():
                print(f'{self.name} {self.surname} учится лучше, чем {other_student.name} {other_student.surname}')
            else:
                print(f'{self.name} {self.surname} учится хуже, чем {other_student.name} {other_student.surname}')

    def __eq__(self, other_student):
        if not isinstance(other_student, Student):
            print('Такого студента нет')
            return
        else:
            if self.student_average_rating() == other_student.student_average_rating():
                print(f'{self.name} {self.surname} и {other_student.name} {other_student.surname} учатся одинаково.')


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.course_grades = {}
        self.study_course = []

    def __str__(self):
        return f'Лектор \n' \
               f'Имя: {self.name} \n' \
               f'Фамилия: {self.surname}\n' \
               f'Средняя оценка за лекции: {self.lecturer_average_rating()} \n'

    def lecturer_average_rating(self):
        val_list = []
        for val in self.course_grades.values():
            val_list += val
        return round((sum(val_list)/len(val_list)),  2)

    def __gt__(self, other_lecturer):
        if not isinstance(other_lecturer, Lecturer):
            print('Такого лектора нет')
            return
        else:
            if self.lecturer_average_rating() > other_lecturer.lecturer_average_rating():
                print(f'{self.name} {self.surname} читает лучше, чем {other_lecturer.name} {other_lecturer.surname}')
            else:
                print(f'{self.name} {self.surname} читает хуже, чем {other_lecturer.name} {other_lecturer.surname}')

    def __eq__(self, other_lecturer):
        if not isinstance(other_lecturer, Lecturer):
            print('Такого лектороа нет')
            return
        else:
            if self.lecturer_average_rating() == other_lecturer.lecturer_average_rating():
                print(f'{self.name} {self.surname} и {other_lecturer.name} {other_lecturer.surname} читают одинаково')


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Проверяющий \n' \
               f'Имя: {self.name} \n' \
               f'Фамилия: {self.surname}\n'


best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student2 = Student('Ben', 'Goodman', 'male')

best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['Java']
best_student.finished_courses += ['Введение в программирование']

best_student2.courses_in_progress += ['Python']
best_student2.courses_in_progress += ['Java']
best_student2.finished_courses += ['Введение в программирование-2']

cool_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer2 = Reviewer('Tom', 'Biddy')

cool_reviewer.courses_attached += ['Python']
cool_reviewer.courses_attached += ['Java']
cool_reviewer2.courses_attached += ['Python']
cool_reviewer2.courses_attached += ['Java']

cool_lecturer = Lecturer('Василий', 'Иванов')
cool_lecturer2 = Lecturer('Сергей', 'Пешкин')

cool_lecturer.study_course += ['Python']
cool_lecturer.study_course += ['Java']
cool_lecturer2.study_course += ['Python']
cool_lecturer2.study_course += ['Java']

cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 9)
cool_reviewer.rate_hw(best_student, 'Java', 8)
cool_reviewer.rate_hw(best_student, 'Java', 7)

cool_reviewer2.rate_hw(best_student2, 'Python', 10)
cool_reviewer2.rate_hw(best_student2, 'Python', 9)
cool_reviewer2.rate_hw(best_student2, 'Java', 8)
cool_reviewer2.rate_hw(best_student2, 'Java', 7)

best_student.rate_courses(cool_lecturer, 'Python', 9)
best_student.rate_courses(cool_lecturer, 'Python', 8)
best_student.rate_courses(cool_lecturer, 'Java', 7)
best_student.rate_courses(cool_lecturer, 'Java', 6)

best_student2.rate_courses(cool_lecturer2, 'Python', 5)
best_student2.rate_courses(cool_lecturer2, 'Python', 4)
best_student2.rate_courses(cool_lecturer2, 'Java', 3)
best_student2.rate_courses(cool_lecturer2, 'Java', 2)

print()
print(cool_reviewer)
print(cool_lecturer)
print(best_student)
print()
print('==========')
print(f'Средняя оценка {best_student.name} {best_student.surname} : {best_student.student_average_rating()}')
print(f'Средняя оценка {best_student2.name} {best_student2.surname} : {best_student2.student_average_rating()}')
if best_student.student_average_rating() > best_student2.student_average_rating():
    print(best_student > best_student2)
elif best_student.student_average_rating() < best_student2.student_average_rating():
    print(best_student < best_student2)
elif best_student.student_average_rating() == best_student2.student_average_rating():
    print(best_student == best_student2)

print('==========')
print(f'Средняя оценка {cool_lecturer.name} {cool_lecturer.surname} : {cool_lecturer.lecturer_average_rating()}')
print(f'Средняя оценка {cool_lecturer2.name} {cool_lecturer2.surname} : {cool_lecturer2.lecturer_average_rating()}')
if cool_lecturer.lecturer_average_rating() > cool_lecturer2.lecturer_average_rating():
    print(cool_lecturer > cool_lecturer2)
elif cool_lecturer.lecturer_average_rating() < cool_lecturer2.lecturer_average_rating():
    print(cool_lecturer < cool_lecturer2)
elif cool_lecturer.lecturer_average_rating() == cool_lecturer2.lecturer_average_rating():
    print(cool_lecturer == cool_lecturer2)