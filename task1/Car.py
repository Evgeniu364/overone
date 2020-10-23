class Car:
    def __init__(self, color, speed, model):
        self.__model = model
        self.__color = color
        self.__speed = speed

    def get_color(self):
        return self.__color

    def get_model(self):
        return self.__model

    def get_speed(self):
        return self.__speed

    def set_color(self, color):
        if type(color) == str:
            self.__color = color


    def __str__(self):
        return f'model - {self.__model}, speed - {self.__speed}, color - {self.__color}'

