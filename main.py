def average_grade_students(list_student, course):
    sum = 0
    kol = 0
    for student in list_student:
        if isinstance(student, Student) and course in student.grades.keys():
            grades = student.grades[course]
            for i in range(len(grades)):
                sum += grades[i]
                kol += 1
    print(f'Среднняя оценка студентов за домашние задания по курсу {course}: {sum / kol}')


def average_grade_lecturers(list_lecturer, course):
    sum = 0
    kol = 0
    for lecturer in list_lecturer:
        if isinstance(lecturer, Lecturer) and course in lecturer.grades.keys():
            grades = lecturer.grades[course]
            for i in range(len(grades)):
                sum += grades[i]
                kol += 1
    print(f'Среднняя оценка лекторов за лекции по курсу {course}: {sum / kol}')


class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self._average_grade()}\nКурсы в процессе изучения: {", ".join(self.courses_in_progress)}\nЗавершенные курсы: {", ".join(self.finished_courses)} '
        return res

    def _average_grade(self):
        sum = 0
        kol = 0
        for grade in self.grades.values():
            for i in range(len(grade)):
                sum += grade[i]
                kol += 1
        return (sum / kol)


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __str__(self):
        res = (f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self._average_grade()}')
        return res

    def __lt__(self, other):
        if isinstance(other, Lecturer):
            return self._average_grade() < other._average_grade()

    def _average_grade(self):
        sum = 0
        kol = 0
        for grade in self.grades.values():
            for i in range(len(grade)):
                sum += grade[i]
                kol += 1
        return (sum / kol)


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
        res = f'Имя: {self.name}\nФамилия: {self.surname}'
        return res


student1 = Student('Ruoy', 'Eman', 'your_gender')
student2 = Student('Roy', 'Johns', 'your_gender')
lecturer1 = Lecturer('Some', 'Buddy')
lecturer2 = Lecturer('Some', 'Buddy')
reviewer1 = Reviewer('Some', 'Buddy')
reviewer2 = Reviewer('Some', 'Buddy')

student1.courses_in_progress += ['Python']
student1.courses_in_progress += ['ООП']
student1.finished_courses += ['Git']
student1.finished_courses += ['Введение в программирование']

student2.courses_in_progress += ['Python']
student2.courses_in_progress += ['ООП']
student2.courses_in_progress += ['Git']
student2.finished_courses += ['Введение в программирование']

reviewer1.courses_attached += ['Python']
reviewer2.courses_attached += ['ООП']

lecturer1.courses_attached += ['Python']
lecturer2.courses_attached += ['ООП']

student1.rate_hw(lecturer1, 'Python', 9)
student1.rate_hw(lecturer2, 'ООП', 8)
student1.rate_hw(lecturer1, 'Python', 6)
student2.rate_hw(lecturer2, 'ООП', 5)
student2.rate_hw(lecturer1, 'Python', 10)
student2.rate_hw(lecturer2, 'ООП', 10)

reviewer1.rate_hw(student1, 'Python', 10)
reviewer1.rate_hw(student1, 'Python', 10)
reviewer1.rate_hw(student1, 'Python', 10)

reviewer2.rate_hw(student2, 'ООП', 7)
reviewer2.rate_hw(student2, 'ООП', 8)
reviewer2.rate_hw(student2, 'ООП', 10)

list_student = [student1, student2]
list_lecturer = [lecturer1, lecturer2]

average_grade_students(list_student, 'ООП')
average_grade_lecturers(list_lecturer, 'Python')
