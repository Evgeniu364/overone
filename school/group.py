from school.student import Student
from school.teacher import Teacher


class Group:
    def __init__(self, number, students: list, teachers: list):
        self.__number = number
        self.__students = students
        self.__teachers = teachers

    def __str__(self):
        return f'{self.__number}'

    @property
    def students(self):
        return self.__students

    @property
    def teachers(self):
        return self.__teachers

    def add_student(self, student):
        if type(student) == Student:
            self.__students.append(student)
            return True
        else:
            return False

    def remove_student(self, name, last_name):
        for i in self.__students:
            if i.name == name and i.last_name == last_name:
                self.__students.remove(i)
                return True

        return False

    def add_teacher(self, teacher):
        if type(teacher) == Teacher:
            self.__teachers.append(teacher)
            return True
        else:
            return False

    def remove_teacher(self, name, last_name):
        for i in self.__teachers:
            if i.name == name and i.last_name == last_name:
                self.__teachers.remove(i)
                return True

        return False

# s1 = Student("Ivan", "Petrov", 19, 4)
# s2 = Student("Petr", "Petrov", 19, 4)
# t1 = Teacher("Alex", "Sidorov", 76, 34)
# t2 = Teacher("Semen", "Sidorov", 34, 4)
# 
# g1 = Group(1, [s1, s2], [t1, t2])
# print(g1)
# g1.add_student(Student("Max", "Ivanov", 19, 8.1))
# g1.remove_student("Petr", "Petrov")
# for i in g1.students:
#     print(i)
# 
# print(g1.add_teacher(Teacher("Max", "Ivanov", 39, 19)))
# for i in g1.teachers:
#     print(i)
