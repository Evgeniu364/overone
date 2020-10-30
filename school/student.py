class Student:
    def __init__(self, name, last_name, age, average_score):
        self.__name = name
        self.__last_name = last_name
        self.__age = age
        self.__average_score = average_score
    
    def __str__(self):
        return f'name: {self.__name}, last name: {self.__last_name}, age: {self.__age}, average score: {self.__average_score}'
    
    @property
    def name(self):
        return self.__name

    @property
    def last_name(self):
        return self.__last_name

    @property
    def age(self):
        return self.__age

    @property
    def average_score(self):
        return self.__average_score
    
    @average_score.setter
    def average_score(self, other):
        self.__average_score = other
