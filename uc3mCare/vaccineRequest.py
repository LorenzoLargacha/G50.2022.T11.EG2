import json
from datetime import datetime
#import pandas

class vaccineRequest:
    def __init__(self, idCode, phoneNumber):
        self.phoneNumber = phoneNumber
        self.idcode = idCode
        JUSTNOW = datetime.utcnow()
        self.timeStamp = datetime.timestamp(JUSTNOW)


    def __str__(self):
        return "VaccineRequest:" + json.dumps(self.__dict__)

    @property
    def phone(self):
        return self.phoneNumber
    @phone.setter
    def phone(self, value):
        self.phoneNumber = value

    @property
    def iddocument(self):
        return self.idcode
    @iddocument.setter
    def iddocument(self, value):
        self.idcode = value
