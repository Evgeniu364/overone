from school.human import Human


class Student(Human):
    def __init__(self, name, last_name, age, average_score):
        # Human.__init__(self, name, last_name, age)
        super().__init__(name, last_name, age)
        self.__average_score = average_score

    def __str__(self):
        return f'name: {self._name}, last name: {self._last_name}, age: {self._age}, average score: {self.__average_score}'


    @property
    def average_score(self):
        return self.__average_score
    
    @average_score.setter
    def average_score(self, other):
        self.__average_score = other

