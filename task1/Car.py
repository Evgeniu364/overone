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

    def increase_speed(self, speed_up):
        if type(speed_up) == int and speed_up > 0:
            self.__speed += speed_up
            return True
        return False

    def decrease_in_speed(self, speed_down):
        if type(speed_down) == int and speed_down > 0:
            self.__speed -= speed_down
            return True
        return False
    
    def change_color(self, new_color):
        if type(new_color) == str:
            self.__color = new_color
            return True
        return False
            
    def __str__(self):
        return f'model - {self.__model}, speed - {self.__speed}, color - {self.__color}'
