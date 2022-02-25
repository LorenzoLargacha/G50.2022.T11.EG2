class vaccineManagementException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

    @property
    def message(self):
        return self.message

    @message.setter
    def message(self, value):
        self.message = value
