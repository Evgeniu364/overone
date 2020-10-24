class Human:
    def __init__(self, name, last_name, age, birth_day):
        self.__name = name
        self.__last_name = last_name
        self.__age = age
        self._birth_day = birth_day

    def __str__(self):
        return f'{self.__name}, {self.__last_name}, {self.__age}, {self._birth_day}'

    def move(self):
        print(self, "передвигается")

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        self.__name = new_name

h = Human("Yauheni", "Petrov", 111, "123123")
print(h.name)




