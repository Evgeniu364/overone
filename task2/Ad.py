import datetime


class Ad:
    def __init__(self, title, description, author):
        self.__title = title
        self.__description = description
        self.__author = author
        self.__date = datetime.datetime.today()
        self.__counter_view = 0

    def __str__(self):
        return f'{self.__title} \n{self.__author} \n{self.__date} \n{self.__counter_view} ' \
            f'\n{self.__description}'
    


