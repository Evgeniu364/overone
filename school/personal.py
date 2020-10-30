from school.human import Human


class Personal(Human):
    def __init__(self, name, last_name, age, duties):
        super().__init__(name, last_name, age)
        self.__duties = duties
    
    def __str__(self):
        return f'name: {self._name}, last name: {self._last_name}, duties {self.__duties}'
