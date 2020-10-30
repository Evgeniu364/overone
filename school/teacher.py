from school.human import Human


class Teacher(Human):
    def __init__(self, name, last_name, age, work_experience):
        super().__init__(name, last_name, age)
        self.__work_experience = work_experience

    def __str__(self):
        return f'name: {self._name}, last name: {self._last_name}, age: {self._age}, work experience: {self.__work_experience}'

