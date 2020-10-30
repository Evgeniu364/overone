class Human:
    def __init__(self, name, last_name, age):
        self._name = name
        self._last_name = last_name
        self._age = age

    def __str__(self):
        return f'name: {self._name}, last name: {self._last_name}, age: {self._age}'

    @property
    def name(self):
        return self._name

    @property
    def last_name(self):
        return self._last_name

    @property
    def age(self):
        return self._age