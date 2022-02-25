import json
from datetime import datetime
import pandas

class vaccineRequest:
    def __init__(self, idCode, phoneNumber):
        self.__phoneNumber = phoneNumber
        self.__idcode = idCode
        JUSTNOW = datetime.utcnow()
        self.__timeStamp = datetime.timestamp(JUSTNOW)

    def __str__(self):
        return "VaccineRequest:" + json.dumps(self.__dict__)

    @property
    def __phone(self):
        return self.__phoneNumber
    @__phone.setter
    def __phone(self, value):
        self.__phoneNumber = value

    @property
    def __iddocument(self):
        return self.__idcode
    @__iddocument.setter
    def __iddocument(self, value):
        self.__idcode = value
