class vaccineManagementException(Exception):
    def __init__(self, message):
        self.__message = message
        super().__init__(self.__message)

    @property
    def __message(self):
        return self.__message

    @__message.setter
    def __message(self, value):
        self.__message = value
